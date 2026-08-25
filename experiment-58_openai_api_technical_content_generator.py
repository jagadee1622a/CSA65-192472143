"""OpenAI API Technical Content Generator\nGenerate short technical content using the OpenAI API.\n"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
prompt = input("Enter your prompt: ")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
