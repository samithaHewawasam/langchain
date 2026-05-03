import urllib.error
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain_core.tools import tool
import certifi
import requests

SYSTEM_PROMPT = """You are a literary data assistant.

## Capabilities

- `fetch_text_from_url`: loads document text from a URL into the conversation.
Do not guess line counts or positions—ground them in tool results from the saved file."""

@tool
def fetch_text_from_url(url: str) -> str:
    """Fetch the document from a URL.
    """
    try:
        resp = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
            verify=certifi.where()
        )
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        return f"Fetch failed: {e}"

model = init_chat_model(
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    model_provider="bedrock_converse",
    temperature=0.5,
    timeout=300,
    max_tokens=25000,
)

checkpointer = InMemorySaver()


agent = create_agent(
    model=model,
    tools=[fetch_text_from_url],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

result = agent.invoke(                                                                                                                                                                                             
      {"messages": [("user", "Fetch text from https://en.wikipedia.org/wiki/SriLankan_Airlines")]},                                                                                                                                               
      config={"configurable": {"thread_id": "1"}}                                                                                                                                                                    
)  

print(result["messages"][-1].content)
