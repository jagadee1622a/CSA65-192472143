"""Prompt Response Comparison\nGenerate and compare multiple LLM responses.\n"""

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
topic = input("Topic/task: ")

prompts = [
    f"Explain {topic} clearly for an engineering student.",
    f"Give a concise structured explanation of {topic}.",
    f"Explain {topic} with key concepts, applications, and limitations."
]

for i, prompt in enumerate(prompts, 1):
    result = generator(prompt, max_new_tokens=120, return_full_text=False)
    print(f"\nPrompt {i}:\n{result[0]['generated_text']}")
