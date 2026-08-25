from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# Load pre-trained embedding model
# --------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------------------
# Technical document collection
# --------------------------------------------------

documents = [
    "Artificial intelligence enables computers to learn from data "
    "and make intelligent decisions.",

    "Machine learning algorithms can identify patterns in large "
    "datasets and make predictions.",

    "Cloud computing provides on-demand access to computing "
    "resources such as servers, storage, and databases.",

    "Cybersecurity protects computer networks and systems from "
    "unauthorized access and cyber attacks.",

    "Database management systems are used to store, organize, "
    "retrieve, and manage large amounts of information.",

    "Computer networks allow multiple devices to communicate "
    "and share data and resources.",

    "Deep learning uses neural networks with multiple layers "
    "to solve complex artificial intelligence problems."
]


# --------------------------------------------------
# User query
# --------------------------------------------------

query = "How can computers learn patterns from information?"


# --------------------------------------------------
# Generate document embeddings
# --------------------------------------------------

document_embeddings = model.encode(documents)


# --------------------------------------------------
# Generate query embedding
# --------------------------------------------------

query_embedding = model.encode([query])


# --------------------------------------------------
# Calculate cosine similarity
# --------------------------------------------------

similarity_scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]


# --------------------------------------------------
# Combine documents and similarity scores
# --------------------------------------------------

results = list(zip(documents, similarity_scores))


# Sort results from highest to lowest similarity
results.sort(key=lambda x: x[1], reverse=True)


# --------------------------------------------------
# Display results
# --------------------------------------------------

print("=" * 70)
print("           SEMANTIC SIMILARITY SEARCH")
print("=" * 70)

print("\nQuery:")
print(query)

print("\nMost Relevant Documents:")
print("-" * 70)

for rank, (document, score) in enumerate(results, start=1):

    print(f"\nRank {rank}")
    print(f"Similarity Score: {score:.4f}")
    print(f"Document: {document}")

    # Display top 3 documents only
    if rank == 3:
        break