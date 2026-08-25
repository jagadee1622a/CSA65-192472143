"""AI Workshop Social Media Post\nGenerate and compare social media posts using prompting strategies.\n"""

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompts = {
    "ZERO-SHOT": """Generate and compare social media posts using prompting strategies.""",
    "ONE-SHOT": """Example: Write clear, concise content for students.
Now perform Generate and compare social media posts using prompting strategies.""",
    "FEW-SHOT": """Example 1: Use a clear professional style.
Example 2: Use concise, complete wording.
Now perform Generate and compare social media posts using prompting strategies."""
}

for title, prompt in prompts.items():
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
    result = generator(
        prompt,
        max_new_tokens=180,
        do_sample=True,
        temperature=0.7,
        return_full_text=False
    )
    print(result[0]["generated_text"])
