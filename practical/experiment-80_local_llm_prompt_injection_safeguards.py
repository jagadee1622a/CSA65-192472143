"""Local LLM Prompt Injection Safeguards\nDemonstrate prompt injection and apply safeguards.\n"""

# Responsible-AI demonstration.
# Do not provide secrets or real sensitive data.
system_instruction = "Answer technical questions accurately. If information is missing, say so."
user_input = input("Enter a test instruction: ")

if any(word in user_input.lower() for word in ["ignore previous", "reveal system prompt", "show secret"]):
    print("Blocked: potentially unsafe prompt-injection instruction.")
else:
    print(system_instruction)
    print("Accepted input:", user_input)
