from google.adk.agents import Agent
from src.utils.config import MODEL # Import the model name from config file

root_agent = Agent(
    name="Rag-Agent",
    model=MODEL,
    description="Vertex AI RAG agent for answering questions",
    tools=[

    ],
    instruction='You are a helpful assistant that answers questions based on the context provided.'
)