"""Engineering Speech To Text\nConvert a spoken engineering question into text.\n"""

import whisper

model = whisper.load_model("base")
audio_file = input("Enter audio file path: ")

result = model.transcribe(audio_file)
print("Transcription:", result["text"])
