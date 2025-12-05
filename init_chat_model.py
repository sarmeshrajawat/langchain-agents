import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model= init_chat_model(
    "gpt-4.1-mini"
    ,temperature= 0.1)

conversation = [
    SystemMessage(content="You're a helpful assistant for question regarding programming"),
    HumanMessage(content="What is python?"),
    AIMessage("Python is a programming language that lets you work quickly and integrate systems more effectively."),
    HumanMessage(content="Who created it?")
]

response = model.invoke('Hello, what is python')

print(response)
print(response.content)