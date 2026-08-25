"""Technical Document AI Assistant\nAnswer questions from project reports and technical manuals.\n"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "The library provides access to technical books and digital journals.",
    "The examination cell publishes examination schedules and results.",
    "The computer laboratory provides systems and network access.",
    "Departments conduct academic and engineering project activities."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
query = input("Student question: ")
scores = cosine_similarity(
    model.encode([query]),
    model.encode(documents)
)[0]

best = scores.argmax()
print("Relevant document:", documents[best])
print("Similarity:", round(float(scores[best]), 4))
