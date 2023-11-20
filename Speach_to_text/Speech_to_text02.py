import speech_recognition as sr

r = sr.Recognizer()
# here i use listen method
with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(f"You said {text}")

    
       
