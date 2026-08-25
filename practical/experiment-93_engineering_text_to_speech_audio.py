"""Engineering Text To Speech Audio\nConvert study material to speech and save an audio file.\n"""

from gtts import gTTS

text = input("Enter engineering text: ")
tts = gTTS(text=text, lang="en")
tts.save("engineering_audio.mp3")
print("Saved as engineering_audio.mp3")
