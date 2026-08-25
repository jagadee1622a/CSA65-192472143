"""Technical Article 50 Word Summary\nSummarize an article using three prompting strategies.\n"""

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompts = {
    "ZERO-SHOT": """Summarize an article using three prompting strategies.""",
    "ONE-SHOT": """Example: Write clear, concise content for students.
Now perform Summarize an article using three prompting strategies.""",
    "FEW-SHOT": """Example 1: Use a clear professional style.
Example 2: Use concise, complete wording.
Now perform Summarize an article using three prompting strategies."""
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
