"""Context Aware LangChain Chatbot\nMaintain context across follow-up questions using retrieval and an LLM.\n"""

# LangChain/RAG starter
# Install the packages listed in requirements.txt before running.
from langchain_core.documents import Document

documents = [
    Document(page_content="Engineering manuals contain technical procedures."),
    Document(page_content="Maintenance should follow approved safety instructions.")
]

print("Loaded", len(documents), "documents.")
print("Next step: connect a vector store and an LLM for retrieval-augmented answers.")
