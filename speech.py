import speech_recognition as rc
import keyboard

r = rc.Recognizer()

with rc.Microphone() as source:
    print("Speak: ")
    audio = r.listen(source)

with rc.Microphone() as source:
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print("Sorry, could not recognize your voice.")
#https://www.youtube.com/watch?v=K_WbsFrPUCk
