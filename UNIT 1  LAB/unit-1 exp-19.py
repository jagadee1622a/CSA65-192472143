from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "The future of Artificial Intelligence"

output = generator(prompt,max_length=60)

print(output[0]["generated_text"])
