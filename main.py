import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

@tool("get weather", description="Get the current weather for a given city.",return_direct=False)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

agent = create_agent(
    model='gpt-4.1-mini',
    tools=[get_weather],
    system_prompt="You're a helpful assistant that provides weather information."
)

response=agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'What is the weather like in New York City?'}
    ]
})

print(response)
print(response['messages'][-1]['content'])

