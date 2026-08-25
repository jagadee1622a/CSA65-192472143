"""Engineering Report Summarization\nSummarize a lengthy engineering report using a pre-trained model.\n"""

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = input("Enter article/report text: ")
result = summarizer(text, max_length=100, min_length=30, do_sample=False)
print("Summary:", result[0]["summary_text"])
