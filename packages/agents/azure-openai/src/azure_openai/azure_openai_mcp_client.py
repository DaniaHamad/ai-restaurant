from dotenv import load_dotenv
from openai import AzureOpenAI
import os
import json
from mcp import ClientSession, StdioServerParameters
from contextlib import AsyncExitStack
from typing import Optional
from mcp.client.stdio import stdio_client
import asyncio
from pathlib import Path

load_dotenv()
class AzureOpenAIMCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None 
        self.exit_stack = AsyncExitStack()

        self.azure_openai = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    async def connect_to_server(self, server_script_path: str):

        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")
        
        if is_python:
            path = Path(server_script_path).resolve()
            server_params = StdioServerParameters(
                command="python",
                args=[str(path)],
                env=None,
            )
        else:
            server_params = StdioServerParameters(
                command="node", args=[server_script_path], env=None
            )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])
    
    
    async def process_query(self, query: str) -> str:
        messages = [
        {
            "role": "user",
            "content": query
        }
    ]
        response = await self.session.list_tools()
        
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": getattr(tool, "inputSchema", {})
            }
        } for tool in response.tools]
        
        response = self.azure_openai.chat.completions.create(
            messages=messages,
            max_completion_tokens=16384,
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            tools=available_tools
    )
        final_text = []
        # The OpenAI API returns a list of choices, each with a message
        choice = response.choices[0]
        message = choice.message
        # If the model responds with a tool call, handle it
        if hasattr(message, "tool_calls") and message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                # Parse arguments from JSON string to dict
                tool_args = json.loads(tool_call.function.arguments)
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")
                messages.append({
                    "role": "assistant",
                    "content": result.content
                })
                # Re-run the model with the new messages
                response = self.azure_openai.chat.completions.create(
                    messages=messages,
                    max_completion_tokens=16384,
                    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
                    tools=available_tools
                )
                choice = response.choices[0]
                message = choice.message
                if hasattr(message, "content") and message.content:
                    final_text.append(message.content)
        else:
            if hasattr(message, "content") and message.content:
                final_text.append(message.content)
        return "\n".join(final_text)
    
    
    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    
    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: uv run azure_openai_mcp_client.py <path_to_server_script>")
        sys.exit(1)

    client = AzureOpenAIMCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())