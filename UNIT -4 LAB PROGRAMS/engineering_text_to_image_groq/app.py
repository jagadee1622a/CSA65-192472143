from flask import Flask, render_template, request, jsonify, send_from_directory
from groq import Groq
from dotenv import load_dotenv
import os
import requests
import urllib.parse
import uuid

load_dotenv()

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "").strip()

GROQ_MODEL = "openai/gpt-oss-20b"
IMAGE_MODEL = "flux"

groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

GENERATED_DIR = os.path.join("static", "generated")
os.makedirs(GENERATED_DIR, exist_ok=True)


def create_detailed_prompt(user_prompt):
    """Use Groq AI to convert a simple idea into a detailed image prompt."""
    if not groq_client:
        return None, "Groq API key is not configured."

    instruction = f"""
You are an expert text-to-image prompt engineer.

Convert the user's engineering image idea into one detailed prompt
for a photorealistic or high-quality technical image.

Include:
- engineering subject
- materials and construction details
- realistic environment
- lighting
- camera angle
- composition
- technical details
- professional engineering visualization style

Do not add text, labels, logos, watermarks, or people unless the user asks.
Return ONLY the final image-generation prompt.

User idea:
{user_prompt}
"""

    try:
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You create precise prompts for engineering text-to-image generation."
                },
                {
                    "role": "user",
                    "content": instruction
                }
            ],
            temperature=0.4,
            max_completion_tokens=500
        )

        prompt = response.choices[0].message.content.strip()

        if not prompt:
            return None, "Groq returned an empty prompt."

        return prompt, None

    except Exception as e:
        print("Groq error:", e)
        return None, f"Groq error: {str(e)}"


def generate_image(prompt):
    """Generate an image using a pre-trained text-to-image model."""
    if not POLLINATIONS_API_KEY:
        return None, "Pollinations API key is not configured."

    encoded_prompt = urllib.parse.quote(prompt, safe="")

    url = (
        f"https://gen.pollinations.ai/image/{encoded_prompt}"
        f"?model={IMAGE_MODEL}&width=1024&height=768"
        f"&safe=true&private=true"
    )

    headers = {
        "Authorization": f"Bearer {POLLINATIONS_API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=300)
        response.raise_for_status()

        filename = f"engineering_{uuid.uuid4().hex}.jpg"
        filepath = os.path.join(GENERATED_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(response.content)

        return f"/static/generated/{filename}", None

    except Exception as e:
        print("Image generation error:", e)
        return None, f"Image generation error: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    user_prompt = str(data.get("prompt", "")).strip()

    if not user_prompt:
        return jsonify({
            "success": False,
            "error": "Please enter an engineering image idea."
        })

    detailed_prompt, error = create_detailed_prompt(user_prompt)

    if error:
        return jsonify({
            "success": False,
            "error": error
        })

    image_url, error = generate_image(detailed_prompt)

    if error:
        return jsonify({
            "success": False,
            "prompt": detailed_prompt,
            "error": error
        })

    return jsonify({
        "success": True,
        "prompt": detailed_prompt,
        "image_url": image_url
    })


if __name__ == "__main__":
    print("=" * 65)
    print("       ENGINEERING TEXT-TO-IMAGE AI")
    print("=" * 65)
    print("Groq key:", "Loaded" if groq_client else "NOT CONFIGURED")
    print("Image API key:", "Loaded" if POLLINATIONS_API_KEY else "NOT CONFIGURED")
    print("Groq model:", GROQ_MODEL)
    print("Image model:", IMAGE_MODEL)
    print("Server: http://127.0.0.1:5000")
    print("=" * 65)

    app.run(debug=True)
