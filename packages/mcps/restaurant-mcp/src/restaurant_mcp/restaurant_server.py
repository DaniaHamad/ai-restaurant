import sys
from mcp.server.fastmcp import FastMCP

class RestaurantServer:
    def __init__(self):
        self.mcp = FastMCP("Hello World")
        print("MCP Server initialized", file=sys.stderr)
        
        # Register MCP tools
        self._register_tools()

    def _register_tools(self):
        # Register your tools here
        @self.mcp.tool()
        def sample_tool(param: str) -> str:
            """A sample tool that echoes the input parameter."""
            return f"Echo: {param}"

    def start(self):
        # execute and return the stdio output
        self.mcp.run(transport="stdio")

server = RestaurantServer().mcp

if __name__ == "__main__":
    server = RestaurantServer()
    server.start()