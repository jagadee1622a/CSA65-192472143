# Engineering Text-to-Image AI with Groq

This project implements the lab experiment:

"Generate an engineering-related image, such as a bridge or robotic
system, from a suitable text prompt using a pre-trained text-to-image model."

## Important architecture

Groq is used for the NLP/prompt-engineering part:
User idea -> Groq AI -> detailed image-generation prompt

A separate pre-trained text-to-image model is then used:
Detailed prompt -> Flux image model -> engineering image

Groq currently provides text generation and vision capabilities, but it
does not provide a native text-to-image generation endpoint. Therefore,
the project uses Groq for intelligent prompt generation and a dedicated
image-generation service for the final image.

## API keys

You need:

1. GROQ_API_KEY
2. POLLINATIONS_API_KEY

Open `.env` and replace the placeholders.

Never share either API key publicly.

## Installation

Open PowerShell in this folder:

python -m venv .venv

Activate:

.\.venv\Scripts\Activate.ps1

If PowerShell blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then:

.\.venv\Scripts\Activate.ps1

Install packages:

python -m pip install -r requirements.txt

## Run

python app.py

Open:

http://127.0.0.1:5000

## Example prompts

- A modern cable-stayed bridge over a river
- A futuristic industrial robotic arm in a smart factory
- An autonomous electric vehicle engineering laboratory
- A large wind turbine farm with electrical equipment
- A modern suspension bridge during sunset

## Workflow

1. User enters an engineering idea.
2. Flask receives the text.
3. Groq generates a detailed image prompt.
4. The prompt is sent to the Flux text-to-image model.
5. The generated image is downloaded.
6. Flask displays the image in the browser.

## Technologies

- Python
- Flask
- Groq API
- Groq LLM
- NLP prompt engineering
- Flux pre-trained text-to-image model
- HTML
- CSS
- JavaScript

## Lab result

The system generates an engineering-related image from a natural-language
text prompt. The generated prompt is also displayed so that the student
can demonstrate the role of the pre-trained language model.

## If your teacher asks "Why Groq?"

Groq is used to understand and expand the user's natural-language idea
into a high-quality image-generation prompt. The final image is produced
by a specialized text-to-image model because Groq's current API is focused
on language inference and multimodal understanding rather than native
text-to-image generation.
