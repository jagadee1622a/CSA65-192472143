# Engineering Support AI Chatbot

A technical engineering-support chatbot using NLP keyword retrieval and a Groq-hosted large language model.

## Features

- Natural-language technical questions
- NLP keyword extraction/retrieval
- Engineering knowledge base
- Groq AI response generation
- Programming troubleshooting
- Electronics and electrical support
- Computer science and networking explanations
- Step-by-step solutions
- Conversation history
- Responsive web interface

## Setup

### 1. Create a Groq API key

Create an API key from the Groq Console.

Never share your API key publicly.

### 2. Add your API key

Open `.env`.

Change:

GROQ_API_KEY=your_groq_api_key_here

to your real key:

GROQ_API_KEY=gsk_your_real_key

### 3. Create a virtual environment

PowerShell:

python -m venv .venv

Activate:

.\.venv\Scripts\Activate.ps1

If PowerShell blocks activation, run:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then activate again:

.\.venv\Scripts\Activate.ps1

### 4. Install dependencies

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

### 5. Run

python app.py

Open:

http://127.0.0.1:5000

## Project structure

engineering_support_groq_chatbot/
|
|-- app.py
|-- engineering_knowledge.json
|-- .env
|-- .env.example
|-- .gitignore
|-- requirements.txt
|-- README.md
|
|-- templates/
|   `-- index.html
|
`-- static/
    `-- style.css

## NLP component

The chatbot performs simple NLP-based keyword retrieval before sending the relevant engineering context to the Groq model.

For a larger project, this can be upgraded to:
- TF-IDF
- Sentence Transformers
- FAISS
- ChromaDB
- RAG with PDF engineering manuals

## Important

The included knowledge base is sample engineering content. You can edit `engineering_knowledge.json` and add your own laboratory manuals, syllabus topics, formulas, troubleshooting guides and technical FAQs.
