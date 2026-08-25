"""Gemini Python Code Generator\nGenerate responses for computational prompts using Gemini.\n"""

import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
prompt = input("Enter your prompt: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
