"""Hugging Face Inference API Text Generation\nGenerate text through a hosted Hugging Face model.\n"""

# Hugging Face hosted inference example.
# Set HF_TOKEN in your environment before running.
import os
from huggingface_hub import InferenceClient

client = InferenceClient(token=os.environ.get("HF_TOKEN"))
prompt = input("Enter prompt: ")

result = client.text_generation(prompt, model="HuggingFaceH4/zephyr-7b-beta", max_new_tokens=120)
print(result)
