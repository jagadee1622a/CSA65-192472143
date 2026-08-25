"""Structured Python Code Generation\nGenerate and validate Python programs from structured prompts.\n"""

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

schema = input("Database schema / programming requirements: ")
task = input("Task: ")

prompt = f"""Use this information:
{schema}

Task:
{task}

Return a concise solution."""
print(generator(prompt, max_new_tokens=180, return_full_text=False)[0]["generated_text"])
