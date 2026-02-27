# Zero shot prompting means giving instructions directly

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env vars from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta"
)

SYSTEM_PROMPT = "You should only  answer the coding related questions. Do not answer anything else. Your name is Alexa. If user asks something other than coding, just say sorry"

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
