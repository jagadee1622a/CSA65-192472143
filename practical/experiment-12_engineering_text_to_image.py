"""Engineering Text To Image\nGenerate an engineering-related image from a text prompt.\n"""

# Text-to-image starter.
# A model/provider is required. This example uses Diffusers.
from diffusers import StableDiffusionPipeline
import torch

prompt = "A detailed engineering concept of a modern robotic bridge inspection system"
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
image = pipe(prompt).images[0]
image.save("engineering_concept.png")
print("Saved engineering_concept.png")
