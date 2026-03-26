import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time

engine = pyttsx3.init()
#adjusting the speed
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 60)

def speak(text):
    print(f"Jarvis: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.3)
    except:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.3)

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning! I am Jarvis. How can I help you today?")
    elif hour < 18:
        speak("Good Afternoon! I am Jarvis. How can I help you today?")
    else:
        speak("Good Evening! I am Jarvis. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 5.0
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, could you repeat that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def run_jarvis():
    chrome_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome = webbrowser.BackgroundBrowser(chrome_path)
    wish_user()
    while True:
        query = take_command()
        if query == "":
            continue
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                for sentence in result.split('. '):
                    speak(sentence)
            except:
                speak("Sorry, I couldn't find anything.")
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            chrome.open("https://www.youtube.com/")
            time.sleep(0.5)
        elif 'open google' in query:
            speak("Opening Google...")
            chrome.open("https://www.google.com/")
            time.sleep(0.5)
        elif 'open gmail' in query:
            speak("Opening Gmail")
            chrome.open("https://www.gmail.com/")
            time.sleep(0.5)
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, could you repeat that?")
            time.sleep(0.3)

def main():
    speak("Jarvis is starting up...")
    time.sleep(0.5)
    run_jarvis()

if __name__ == "__main__":
    main()