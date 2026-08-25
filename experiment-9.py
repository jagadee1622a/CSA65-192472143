from transformers import pipeline

# Load the pre-trained GPT-2 model
writer = pipeline(
    "text-generation",
    model="gpt2"
)

# Engineering-related prompt
prompt = """
Artificial Intelligence is transforming modern engineering by
"""

# Generate text
result = writer(
    prompt,
    max_new_tokens=100,
    num_return_sequences=1,
    temperature=0.7,
    do_sample=True
)

# Display output
print("=" * 70)
print("             AI ENGINEERING WRITING ASSISTANT")
print("=" * 70)

print("\nPrompt:")
print(prompt)

print("\nGenerated Output:")
print(result[0]["generated_text"])