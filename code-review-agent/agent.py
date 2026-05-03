from langchain.agents import create_agent
from langchain_aws import ChatBedrock

def get_weather(city: str) -> str:
    """Get weather from given city."""
    return f"it's always sunny in {city}!"

model = ChatBedrock(
    model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are helpful assistant"
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)

print(result["messages"][-1].content)