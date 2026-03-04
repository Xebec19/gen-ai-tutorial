# Few Shot Prompting, better than Zero shot prompting. In this type of prompting, u also give examples

# Zero shot prompting means giving instructions directly

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
You're an expert AI Assistant in resolving user queries using chain of thought.
You work on Start, Plan and Output steps.
You need to first Plan what needs to be done. The Plan can be multiple steps.
Once you think enough Plan has been done, finally you can give an Output.

Rules:
- Strictly Follow the given JSON output format
- Only run one step at a time
- The sequence of steps is Start (where user gives an input), Plan (That can be multiple times)
and finally Output (which is going to the displayed to the user).

Output JSON Format:
{ "step": "Start" | "Plan" | "Output", "content": "string" }

Example:
Start: Hey, Can you solve 2 + 3 * 5 / 10
Plan: { "step": "Plan", "content": "Seems like user is interested in math problem 2 + 3 * 5 / 10" }
Plan: { "step": "Plan", "content": "looking at the problem, we should solve the using BODMAS method" }
Plan: { "step": "Plan", "content": "Yes, the BODMAS is correct thing to be done" }
Plan: { "step": "Plan", "content": "first we must multiply 3 * 5 which is 15" }
"""

print("\n\n\n")

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history,
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "Start":
        print("Starting LLM Loop", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "Plan":
        print("Thinking", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "Output":
        print("Done", parsed_result.get("content"))
        break

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": SYSTEM_PROMPT,
        },
        {"role": "user", "content": "Hey I am Rohan Thakur, Who are you ?"},
    ],
)

print(response.choices[0].message.content)

print("\n\n\n")
