"""Local LLM Translation Paraphrasing\nTranslate and paraphrase engineering content locally.\n"""

from transformers import pipeline

paraphraser = pipeline("text2text-generation", model="google/flan-t5-small")
text = input("Engineering text: ")
prompt = f"Paraphrase this engineering text clearly: {text}"
print(paraphraser(prompt, max_new_tokens=150)[0]["generated_text"])
