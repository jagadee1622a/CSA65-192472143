"""Engineering Document Summarizer\nGenerate a concise summary while preserving key information.\n"""

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
document = input("Paste the engineering document: ")

result = summarizer(document, max_length=120, min_length=40, do_sample=False)
print("Summary:", result[0]["summary_text"])
