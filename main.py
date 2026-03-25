import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes

engine = pyttsx3.init()
#check voices later
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def speak(text):
    print(f"Jarvis: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech failed:", e)

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: ", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, could you repeat that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""
    
#function to run Jarvis
def run_jarvis():
    return "Hello I am jarvis"
    
#testing to check if the computer can say stuff
speak("Eda mone")