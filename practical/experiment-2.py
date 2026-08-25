from transformers import pipeline

# Load a text-generation model
generator = pipeline("text-generation", model="gpt2")

# -------------------------------
# 1. ZERO-SHOT PROMPT
# -------------------------------
zero_shot_prompt = """
Write a 200-word blog on "Applications of Artificial Intelligence in Healthcare".
Discuss disease diagnosis, medical imaging, drug discovery, personalized
treatment, patient monitoring, and healthcare administration.
Use simple and informative language for the general public.
"""

# -------------------------------
# 2. ONE-SHOT PROMPT
# -------------------------------
one_shot_prompt = """
Example:
Topic: Applications of Artificial Intelligence in Education.
Blog: Artificial Intelligence is transforming education through personalized
learning, automated assessment, intelligent tutoring, and student performance
analysis.

Now write a 200-word blog on "Applications of Artificial Intelligence in Healthcare".
Discuss diagnosis, medical imaging, drug discovery, personalized treatment,
patient monitoring, and healthcare administration.
"""

# -------------------------------
# 3. FEW-SHOT PROMPT
# -------------------------------
few_shot_prompt = """
Example 1:
Topic: AI in Education.
AI supports personalized learning, automated assessment, intelligent tutoring,
and student performance analysis.

Example 2:
Topic: AI in Transportation.
AI is used for autonomous vehicles, traffic prediction, route optimization,
and transportation safety.

Example 3:
Topic: AI in Banking.
AI helps detect fraud, assess financial risks, provide chatbots, and personalize
financial services.

Now write a 200-word blog on "Applications of Artificial Intelligence in Healthcare".
Discuss diagnosis, medical imaging, drug discovery, personalized treatment,
patient monitoring, and healthcare administration.
Use a clear and informative style.
"""

# Function to generate output
def generate_blog(title, prompt):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    result = generator(
        prompt,
        max_new_tokens=300,
        num_return_sequences=1,
        temperature=0.7,
        do_sample=True
    )

    print(result[0]["generated_text"])


# Generate all three outputs
generate_blog("ZERO-SHOT OUTPUT", zero_shot_prompt)
generate_blog("ONE-SHOT OUTPUT", one_shot_prompt)
generate_blog("FEW-SHOT OUTPUT", few_shot_prompt)