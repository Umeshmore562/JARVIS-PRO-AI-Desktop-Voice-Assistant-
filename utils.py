import datetime
import speech_recognition as sr
from tts import speak

def log(message, output_box=None):
    if output_box:  
        output_box.insert("end", message + "\n")
        output_box.yview("end")
    else:           
        print(message)


def greet(log_func=None):
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!", log_func)
    elif hour < 18:
        speak("Good afternoon!", log_func)
    else:
        speak("Good evening!", log_func)
    speak("I am Jarvis. How can I help you?", log_func)

def take_command(log_func=None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if log_func:
            log_func("🎤 Listening...")
        else:
            print("🎤 Listening...")

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            
            if log_func:
                log_func(f"You said: {query}")  
            else:
                print(f"You said: {query}")

            return query.lower()

        except sr.WaitTimeoutError:
            if log_func:
                speak("No speech detected, please type your command.", log_func)
            else:
                print("No speech detected, please type your command.")
            query = input("You (typed): ")
            return query.lower()

        except Exception:
            if log_func:
                speak("Sorry, I couldn't understand. Please type your command.", log_func)
            else:
                print("Sorry, I couldn't understand. Please type your command.")
            query = input("You (typed): ")
            return query.lower()
