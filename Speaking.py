from gtts import gTTS
import os

tts = gTTS(text='Testing. 1, 2, 3', lang='en')
tts.save("test.mp3")
os.system("aplay test.mp3")