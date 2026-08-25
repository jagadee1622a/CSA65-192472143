"""FAISS Or Chroma Technical Retrieval\nBuild a vector database for technical report retrieval.\n"""

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Machine learning is used in engineering prediction.",
    "Cybersecurity protects computer networks.",
    "Database systems organize and retrieve information.",
    "Artificial intelligence optimizes engineering design."
]

embeddings = model.encode(documents, normalize_embeddings=True).astype("float32")
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

query = input("Enter query: ")
q = model.encode([query], normalize_embeddings=True).astype("float32")

scores, ids = index.search(q, min(3, len(documents)))

for rank, (score, idx) in enumerate(zip(scores[0], ids[0]), 1):
    print(f"Rank {rank} | Score: {score:.4f}")
    print(documents[idx])
