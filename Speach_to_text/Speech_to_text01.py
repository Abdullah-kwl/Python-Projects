import speech_recognition as sr

r = sr.Recognizer()
# here i use record method
print("Please Speek")
with sr.Microphone() as source:
    print("Recognizing...")
    audio = r.record(source,duration=5)
    text = r.recognize_google(audio)
    print(f"You said ==> : {text}")

    
       