"""Student Feedback Contextual Embeddings\nGenerate embeddings before clustering or classification.\n"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Artificial intelligence helps engineers solve complex problems.",
    "Machine learning discovers patterns in engineering data.",
    "Civil engineering focuses on structures and infrastructure."
]

query = "How does AI help engineering?"

embeddings = model.encode(texts)
query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, embeddings)[0]

for rank, (text, score) in enumerate(
    sorted(zip(texts, scores), key=lambda x: x[1], reverse=True), 1
):
    print(f"Rank {rank} | Similarity: {score:.4f}")
    print(text)
    print()
