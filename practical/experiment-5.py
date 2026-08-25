from transformers import pipeline

# Load a pre-trained sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

# Sample student feedback
feedback = [
    "The placement training was excellent and very helpful.",
    "I am disappointed with the placement opportunities provided.",
    "The placement process was okay and completed on time.",
    "The trainers explained everything clearly and professionally.",
    "The placement process was confusing and poorly organized."
]

print("=" * 70)
print("       STUDENT FEEDBACK SENTIMENT ANALYSIS")
print("=" * 70)

# Perform sentiment analysis
for comment in feedback:

    result = sentiment_pipeline(comment)[0]

    label = result["label"]
    score = result["score"]

    print("\nFeedback:", comment)
    print("Sentiment:", label)
    print("Confidence:", round(score, 4))
    print("-" * 70)