from transformers import pipeline

# Load a pre-trained language model
chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

# College information
college_info = """
Engineering College Student Information:

Admissions:
Students can apply for admission by completing the application form
and submitting the required documents according to the college rules.

Examinations:
The examination cell conducts internal assessments and semester
examinations. Examination schedules and results are provided through
the student portal.

Attendance:
Students must maintain the minimum attendance required by the college.
Students can check their attendance through the student portal.

Departments:
The college has Computer Science Engineering, Information Technology,
Electronics and Communication Engineering, Electrical and Electronics
Engineering, Mechanical Engineering, and Civil Engineering departments.

Campus Facilities:
The college provides a central library, computer laboratories,
engineering laboratories, sports facilities, cafeteria, auditorium,
hostels, and Wi-Fi facilities.
"""

print("=" * 65)
print("       ENGINEERING COLLEGE AI CHATBOT")
print("=" * 65)

print("\nAsk about:")
print("Admissions | Examinations | Attendance | Departments | Facilities")
print("Type 'exit' to stop the chatbot.\n")


while True:

    question = input("Student: ")

    if question.lower() == "exit":
        print("Chatbot: Thank you! Have a great day.")
        break

    # Create prompt
    prompt = f"""
You are an engineering college student-support chatbot.

Use the following college information to answer the student's question.

COLLEGE INFORMATION:
{college_info}

STUDENT QUESTION:
{question}

ANSWER:
"""

    # Generate response
    result = chatbot(
        prompt,
        max_new_tokens=80,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.5
    )

    # Extract generated answer
    generated_text = result[0]["generated_text"]

    # Display only the answer portion
    answer = generated_text.split("ANSWER:")[-1].strip()

    print("Chatbot:", answer)
    print()