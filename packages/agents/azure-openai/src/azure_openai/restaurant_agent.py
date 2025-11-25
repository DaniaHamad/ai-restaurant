from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder
import os

class RestaurantAgent:
    def __init__(self):
        self.project = AIProjectClient(
            credential=DefaultAzureCredential(),
            endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"))

        self.agent = self.project.agents.get_agent(os.getenv("AZURE_OPENAI_AGENT"))

        self.thread = self.project.agents.threads.create()
        print(f"Created thread, ID: {self.thread.id}")
    
    def run_agent(self, content: str):
        self.message = self.project.agents.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content
        )
 
        run = self.project.agents.runs.create_and_process(
            thread_id=self.thread.id,
            agent_id=self.agent.id
        )

        if run.status == "failed":
            print(f"Run failed: {run.last_error}")
        else:
            messages = self.project.agents.messages.list(thread_id=self.thread.id, order=ListSortOrder.ASCENDING)

        for message in messages:
            if message.text_messages:
                print(f"{message.role}: {message.text_messages[-1].text.value}")