"""Ollama Local Question Answering\nDemonstrate local LLM question answering through Ollama.\n"""

import requests

prompt = input("Enter your prompt: ")
response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3.2", "prompt": prompt, "stream": False},
    timeout=120
)
response.raise_for_status()
print(response.json()["response"])
