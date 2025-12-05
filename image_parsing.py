from base64 import b64encode
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

load_dotenv()

model= init_chat_model(
    "gpt-4.1-mini")

message = HumanMessage(content=[
    {'type': 'text', 'text': 'Describe the image content.'},
    {
        'type': 'image',
        'base64': b64encode(open('example_image.jpg', 'rb').read()).decode(),
        'mime_type': 'image/avif'    
    }
])

response = model.invoke([message])
print(response.content)