"""Generative AI Engineering Content Generator\nGenerate introduction, concepts, applications, advantages, and conclusion.\n"""

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
topic = input("Engineering topic: ")

prompt = f"""Write structured technical content about {topic}.
Include:
1. Introduction
2. Key concepts
3. Applications
4. Advantages
5. Challenges
6. Conclusion
"""
result = generator(prompt, max_new_tokens=350, return_full_text=False)
print(result[0]["generated_text"])
