import speech_recognition as sr
file_name="s1.wav"
r=sr.Recognizer()

with sr.AudioFile(file_name) as source:
    audio_data=r.record(source)
    text=r.recognize_google(audio_data)
    print(text)
