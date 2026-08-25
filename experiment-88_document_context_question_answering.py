"""Document Context Question Answering\nAnswer only from the supplied engineering document context.\n"""

from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

context = """Engineering laboratories contain computers, measurement tools,
safety equipment, and testing instruments. Students must follow laboratory
safety procedures and instructor instructions."""

question = input("Question: ")
try:
    result = qa(question=question, context=context)
    print("Answer:", result["answer"])
    print("Confidence:", round(result["score"], 4))
except Exception as exc:
    print("Your Transformers installation does not expose the question-answering task.")
    print("Error:", exc)
