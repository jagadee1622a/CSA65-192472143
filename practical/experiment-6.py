from transformers import pipeline

# Load text generation model
generator = pipeline(
    "text-generation",
    model="gpt2"
)


# --------------------------------------------------
# Function to generate product description
# --------------------------------------------------

def generate_description(title, prompt):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    result = generator(
        prompt,
        max_new_tokens=180,
        num_return_sequences=1,
        temperature=0.7,
        do_sample=True
    )

    print(result[0]["generated_text"])


# --------------------------------------------------
# 1. ZERO-SHOT PROMPT
# --------------------------------------------------

zero_shot_prompt = """
Write a product description for a Smart Fitness Watch designed
for engineering college students.

Mention features such as heart-rate monitoring, step counting,
sleep tracking, workout tracking, notifications, battery life,
and water resistance.

Use attractive and simple language suitable for students.
"""


# --------------------------------------------------
# 2. ONE-SHOT PROMPT
# --------------------------------------------------

one_shot_prompt = """
Example:

Product: Smart Backpack
Description:
The Smart Backpack is designed for modern students. It provides
multiple compartments, USB charging, a lightweight design, and
water-resistant material. Its practical features make it useful
for students who travel between classes and carry electronic devices.

Now write a product description for a Smart Fitness Watch designed
for engineering college students.

Mention heart-rate monitoring, step counting, sleep tracking,
workout tracking, notifications, battery life, and water resistance.
Use a similar attractive and student-friendly style.
"""


# --------------------------------------------------
# 3. FEW-SHOT PROMPT
# --------------------------------------------------

few_shot_prompt = """
Example 1:

Product: Smart Backpack
Description:
A lightweight and durable backpack designed for students. It
provides organized storage, USB charging, and water-resistant
protection for everyday college use.


Example 2:

Product: Wireless Earbuds
Description:
Compact wireless earbuds designed for students. They provide
clear sound, long battery life, comfortable fitting, and
convenient controls for study and entertainment.


Example 3:

Product: Smart Water Bottle
Description:
A smart water bottle that helps students stay hydrated. It
provides temperature tracking, reminders, a leak-proof design,
and a rechargeable battery.


Now write a product description for:

Product: Smart Fitness Watch

Target users: Engineering college students.

Include:
- Heart-rate monitoring
- Step counting
- Sleep tracking
- Workout tracking
- Smartphone notifications
- Long battery life
- Water resistance

Use a modern, attractive, concise, and student-friendly style.
"""


# --------------------------------------------------
# Execute all three prompts
# --------------------------------------------------

generate_description(
    "ZERO-SHOT PRODUCT DESCRIPTION",
    zero_shot_prompt
)

generate_description(
    "ONE-SHOT PRODUCT DESCRIPTION",
    one_shot_prompt
)

generate_description(
    "FEW-SHOT PRODUCT DESCRIPTION",
    few_shot_prompt
)