"""Academic Regulations RAG\nBuild RAG for regulations and laboratory manuals.\n"""

# End-to-end RAG starter
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Engineering regulations require students to follow laboratory safety rules.",
    "Academic guidelines describe attendance and examination procedures.",
    "Laboratory manuals contain equipment operation instructions."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
query = input("Question: ")

doc_embeddings = model.encode(documents)
query_embedding = model.encode([query])
scores = cosine_similarity(query_embedding, doc_embeddings)[0]

best = scores.argmax()
print("Retrieved context:", documents[best])
print("Similarity:", round(float(scores[best]), 4))
print("Answer generation can be connected to a local or hosted LLM.")
