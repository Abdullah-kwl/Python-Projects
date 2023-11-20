import speech_recognition as sr




# *******************  Stack Over Flow   *******************


def speech_recog():
    r = sr.Recognizer()

    mic = sr.Microphone()


    while True:
        with mic as source:
            print("Speak...")

            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print(f"You said {text}")

            except sr.UnknownValueError:
                print("Didnt hear that try again")
speech_recog()