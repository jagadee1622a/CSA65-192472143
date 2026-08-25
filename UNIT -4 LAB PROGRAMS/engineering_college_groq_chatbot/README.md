# Engineering College AI Chatbot - Groq API

This project is an AI chatbot for engineering college student queries.

It uses:
- Python
- Flask
- Groq API
- A Groq-hosted LLM
- A local college knowledge base in JSON
- HTML/CSS/JavaScript

## 1. Get a Groq API key

Create a Groq API key from the Groq Console.

Do NOT share your API key publicly.

## 2. Add your API key

Open the `.env` file in this folder.

Change:

GROQ_API_KEY=your_groq_api_key_here

to:

GROQ_API_KEY=YOUR_REAL_GROQ_KEY

Do not add quotes unless necessary.

## 3. Install packages

Open PowerShell in this folder:

python -m pip install -r requirements.txt

## 4. Run

python app.py

You should see:

Groq API key loaded successfully.
Server: http://127.0.0.1:5000

## 5. Open the chatbot

Open this in Chrome:

http://127.0.0.1:5000

## Example questions

- Hi
- What is CSE?
- How much is the college fee?
- When do exams start?
- Tell me about placements
- What is the attendance requirement?
- Tell me about hostel
- What is available in the library?
- How can I get a bonafide certificate?

## Important

The college_data.json file contains sample/general college information.

For your final college project, replace the sample information with your actual college:
- fee structure
- departments
- faculty/HOD details
- exam dates
- placement details
- hostel information
- office contacts
- attendance rules
- timetable information

The chatbot is instructed not to invent official college-specific information when it is not present in the knowledge base.

## Project structure

engineering_college_groq_chatbot/
|
|-- app.py
|-- college_data.json
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
