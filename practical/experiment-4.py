import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download("punkt", quiet=True)

# ---------------------------------------------------
# Engineering Support Knowledge Base
# ---------------------------------------------------

questions = [
    "What is Python programming?",
    "What is a variable in programming?",
    "What is a function?",
    "What is object oriented programming?",
    "What is an IP address?",
    "What is a computer network?",
    "What is TCP?",
    "What is the difference between LAN and WAN?",
    "What is a database?",
    "What is SQL?",
    "What is a primary key?",
    "What is normalization in database?",
    "What is an algorithm?",
    "What is artificial intelligence?",
    "What is machine learning?",
    "What is an operating system?"
]

answers = [
    "Python is a high-level, interpreted programming language known for its simple syntax and wide range of applications.",
    
    "A variable is a named memory location used to store a value that can change during program execution.",
    
    "A function is a reusable block of code designed to perform a specific task. It can accept inputs and return a result.",
    
    "Object-oriented programming is a programming approach based on objects and classes. Its major concepts include inheritance, encapsulation, polymorphism, and abstraction.",
    
    "An IP address is a numerical address assigned to a device on a network. It allows devices to identify and communicate with each other.",
    
    "A computer network is a collection of connected devices that communicate and share resources such as data, applications, and hardware.",
    
    "TCP stands for Transmission Control Protocol. It provides reliable, ordered, and error-checked delivery of data over a network.",
    
    "LAN covers a relatively small geographical area such as a laboratory or building, while WAN connects networks over a larger geographical area.",
    
    "A database is an organized collection of data that can be stored, managed, and retrieved efficiently.",
    
    "SQL stands for Structured Query Language. It is used to create, retrieve, update, and manage data in relational databases.",
    
    "A primary key is a column or set of columns that uniquely identifies each record in a database table.",
    
    "Database normalization is the process of organizing data to reduce redundancy and improve data consistency.",
    
    "An algorithm is a step-by-step procedure used to solve a problem or perform a computation.",
    
    "Artificial Intelligence is a field of computer science that enables machines to perform tasks that normally require human intelligence.",
    
    "Machine learning is a branch of AI in which computers learn patterns from data and use them to make predictions or decisions.",
    
    "An operating system is system software that manages computer hardware and provides services for application programs."
]

# ---------------------------------------------------
# NLP PREPROCESSING
# ---------------------------------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


processed_questions = [preprocess(q) for q in questions]

# ---------------------------------------------------
# Convert questions into TF-IDF vectors
# ---------------------------------------------------

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)


# ---------------------------------------------------
# Chatbot function
# ---------------------------------------------------

def chatbot(user_question):

    cleaned_question = preprocess(user_question)

    # Convert user question to vector
    user_vector = vectorizer.transform([cleaned_question])

    # Calculate cosine similarity
    similarities = cosine_similarity(
        user_vector,
        question_vectors
    )[0]

    # Find best matching question
    best_index = similarities.argmax()
    best_score = similarities[best_index]

    # Minimum confidence threshold
    if best_score < 0.20:
        return (
            "Sorry, I could not understand your question. "
            "Please ask about programming, networking, databases, "
            "or basic engineering concepts."
        )

    return (
        f"{answers[best_index]}\n"
        f"(Confidence: {best_score:.2f})"
    )


# ---------------------------------------------------
# Chatbot Interface
# ---------------------------------------------------

print("=" * 60)
print("       ENGINEERING SUPPORT CHATBOT")
print("=" * 60)

print("Ask questions about:")
print("Programming | Networking | Databases | Engineering")
print("Type 'exit' to stop the chatbot.")

while True:

    user_input = input("\nStudent: ")

    if user_input.lower() == "exit":
        print("Chatbot: Thank you! Goodbye.")
        break

    response = chatbot(user_input)

    print("Chatbot:", response)