"""Campus Facilities Sentiment Classification\nClassify facility comments with a Hugging Face Transformer.\n"""

from transformers import pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

reviews = [
    "The campus facilities are excellent and well maintained.",
    "The facilities are poor and need improvement.",
    "The facilities are adequate."
]

for review in reviews:
    result = sentiment(review)[0]
    print("\nReview:", review)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 4))
