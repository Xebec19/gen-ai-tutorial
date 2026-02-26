import os
from google import genai
from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
