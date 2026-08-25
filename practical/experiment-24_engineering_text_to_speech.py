"""Engineering Text To Speech\nConvert engineering text into speech.\n"""

from gtts import gTTS

text = input("Enter engineering text: ")
tts = gTTS(text=text, lang="en")
tts.save("engineering_audio.mp3")
print("Saved as engineering_audio.mp3")
