import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time

engine = pyttsx3.init()

#check voices later
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

#adjust speaking rate (default is 200)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 60)

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
    time.sleep(5)
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
#still need to fix a lot of things
def run_jarvis():
    chrome_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome')
    wish_user()
    while True:
        query = take_command()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia: " + result)
            except:
                speak("Sorry, I couldn't find anything.")
        elif 'open youtube' in query:
            speak("Openning youtube...")
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Google Opened")
            time.sleep(5)
            continue
        elif 'time' in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {t}")
        elif 'exit' in query or 'bye' in query:
            speak("GoodBye!, Have a great day")
            break
        else:
            speak("Sorry, could you repeat that")
    

def main():
    speak("Eda mone")
    time.sleep(5)
    run_jarvis()

if __name__ == "__main__":
    main()