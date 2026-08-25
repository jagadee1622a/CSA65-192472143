"""Microphone Engineering Speech To Text\nCapture spoken engineering questions and transcribe them.\n"""

import whisper

model = whisper.load_model("base")
audio_file = input("Enter audio file path: ")

result = model.transcribe(audio_file)
print("Transcription:", result["text"])
