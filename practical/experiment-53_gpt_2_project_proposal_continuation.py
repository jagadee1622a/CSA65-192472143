"""GPT 2 Project Proposal Continuation\nGenerate a project proposal continuation using GPT-2.\n"""

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial Intelligence is transforming engineering by"
result = generator(
    prompt,
    max_new_tokens=120,
    do_sample=True,
    temperature=0.7,
    return_full_text=False
)

print(result[0]["generated_text"])
