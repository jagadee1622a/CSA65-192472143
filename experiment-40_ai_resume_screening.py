"""AI Resume Screening\nRank engineering resumes against a job description.\n"""

import subprocess
import tempfile
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
requirement = input("Programming requirement: ")

prompt = f"Write a Python program for this requirement:\n{requirement}\nCode:"
generated = generator(prompt, max_new_tokens=180, return_full_text=False)[0]["generated_text"]
print("Generated solution:\n", generated)

print("\nFor validation, extract the Python code and execute it only in a sandbox.")
