import pyttsx3
import threading
import queue

engine = pyttsx3.init(driverName='sapi5')
tts_queue = queue.Queue()

def tts_worker():
    while True:
        text = tts_queue.get()
        engine.say(text)
        engine.runAndWait()
        tts_queue.task_done()

threading.Thread(target=tts_worker, daemon=True).start()

def speak(text, log_func=None):
    if log_func:
        log_func(f"Jarvis: {text}")   
    tts_queue.put(text)

