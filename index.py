from gtts import gTTS

text = "Hello, welcome to the text-to-speech conversion using gTTS."
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")

print("Audio file 'hello.mp3' has been created successfully.")

#
