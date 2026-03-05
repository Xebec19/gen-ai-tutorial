import os
from dotenv import load_dotenv
from openai import OpenAI
import json

# Load env vars from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta"
)

SYSTEM_PROMPT = """
You are an AI persona Assistant named Piyush Garg.
You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and principle engineer.
Your main tech stack is JS and Python and You are learning GenAI these days.

Examples:
Q. Hey
A: Hey, Whats up!
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": SYSTEM_PROMPT,
        },
        {"role": "user", "content": "Hey I am Rohan Thakur, Who are you ?"},
    ],
)

print(response.choices[0].message.content)
