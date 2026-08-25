"""Indian Language Machine Translation\nTranslate engineering text from English into an Indian language.\n"""

from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-hi"
)

text = input("Enter English engineering text: ")
result = translator(text, max_length=256)
print("Translation:", result[0]["translation_text"])
