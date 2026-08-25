from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Engineering documents
documents = [
    "Machine learning is used in engineering to predict equipment failures "
    "and improve maintenance scheduling.",

    "Finite element analysis is a numerical method used to analyze stress "
    "and deformation in mechanical structures.",

    "Renewable energy systems use solar panels and wind turbines to generate "
    "clean electricity.",

    "Artificial intelligence can optimize engineering design and automate "
    "complex decision-making processes.",

    "Robotics combines mechanical engineering, electronics, and computer "
    "science to build automated machines."
]

# User's natural-language query
query = "How can AI help engineers improve the design process?"

# Convert documents and query into embeddings
document_embeddings = model.encode(documents)
query_embedding = model.encode([query])

# Calculate cosine similarity
similarity_scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

# Sort documents by similarity score
results = sorted(
    zip(documents, similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\nQuery:")
print(query)

print("\nSemantic Search Results:")
print("-" * 70)

for rank, (document, score) in enumerate(results, start=1):
    print(f"\nRank {rank}")
    print(f"Similarity Score: {score:.4f}")
    print(f"Document: {document}")