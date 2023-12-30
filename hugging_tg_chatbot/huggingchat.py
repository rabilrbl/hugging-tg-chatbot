import os
import requests
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv

load_dotenv()

if os.getenv("HF_EMAIL") and os.getenv("HF_PASSWORD"):
    # Log in to huggingface and grant authorization to huggingchat
    sign = Login(os.getenv("HF_EMAIL"), os.getenv("HF_PASSWORD"))
    cookies = sign.login()
else:
    cookies = requests.get("https://huggingface.co/chat/").cookies

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())


def generate_response(message: str):
    """Generate a response to a message"""
    response_queue = ""
    for resp in chatbot.query(
        message,
        stream=True
    ):
        if resp:
            response_queue += resp["token"]
        if len(response_queue) > 100:
            yield response_queue
            response_queue = ""
    yield response_queue