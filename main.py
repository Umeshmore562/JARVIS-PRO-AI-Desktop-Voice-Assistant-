import tkinter as tk
from tkinter import scrolledtext
import threading, queue, psutil, requests
import datetime as dt
import customtkinter as ctk

import pywhatkit, pyjokes, webbrowser as wb
from tts import speak
from utils import log, greet, take_command
from commands import send_email_interactive, wiki_search, solve_math
from docs import create_word_doc, create_ppt
from config import EMAIL_CONTACTS

# --- Globals ---
jarvis_running = False
task_queue = queue.Queue()
user_input_var = None
gui_queue = queue.Queue()

# --- Safe log ---
def safe_log(msg):
    gui_queue.put(msg)

def gui_update_loop():
    while not gui_queue.empty():
        msg = gui_queue.get()
        output_box.insert(tk.END, msg + "\n")
        output_box.see(tk.END)
    app.after(100, gui_update_loop)

# --- Worker Thread ---
def task_worker():
    while True:
        command = task_queue.get()
        try:
            process_command(command)
        except Exception as e:
            safe_log(f"Error: {e}")
        task_queue.task_done()

threading.Thread(target=task_worker, daemon=True).start()


def process_command(command):
    global jarvis_running

    if 'exit' in command or 'stop' in command:
        speak("Goodbye!", log_func=safe_log)
        jarvis_running = False
        return

    elif 'time' in command:
        current_time = dt.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}", log_func=safe_log)

    elif 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song}", log_func=safe_log)
        pywhatkit.playonyt(song)

    elif 'who is' in command or 'what is' in command or 'tell me about' in command:
        wiki_search(command, log_func=safe_log)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke, log_func=safe_log)

    elif 'search' in command:
        query = command.replace("search", "")
        wb.open(f"https://www.google.com/search?q={query}")
        speak(f"Here are the search results for {query}", log_func=safe_log)

    elif 'open youtube' in command:
        wb.open("https://www.youtube.com")
        speak("Opening YouTube", log_func=safe_log)

    elif 'open google' in command:
        wb.open("https://www.google.com")
        speak("Opening Google", log_func=safe_log)

    elif 'calculate' in command:
        solve_math(command, log_func=safe_log)

    elif 'send email' in command:
        for name in EMAIL_CONTACTS:
            if name in command:
                send_email_interactive(name, log_func=safe_log, typed_input_func=get_typed_input)

    elif 'create word' in command:
        topic = command.replace("create word on", "").strip()
        create_word_doc(topic, log_func=safe_log)

    elif 'create presentation' in command:
        topic = command.replace("create presentation on", "").strip()
        create_ppt(topic, log_func=safe_log)

    else:
        speak("Sorry, I didn't get that.", log_func=safe_log)

# --- Jarvis Control ---
def run_jarvis():
    global jarvis_running
    greet(log_func=safe_log)
    while jarvis_running:
        command = take_command()
        if command != "none":
            task_queue.put(command.lower())

def start_jarvis():
    global jarvis_running
    jarvis_running = True
    threading.Thread(target=run_jarvis, daemon=True).start()

def stop_jarvis():
    global jarvis_running
    jarvis_running = False
    speak("Jarvis stopped.", log_func=safe_log)

def get_typed_input():
    global user_input_var
    user_input_var = tk.StringVar()
    input_box.focus_set()
    app.wait_variable(user_input_var)
    return user_input_var.get()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Jarvis Pro AI Assistant")
app.geometry("1100x680")
app.minsize(900, 600)

BG = "#070e17"
NEON = "#00eaff"
TEXT = "#bdefff"
MUTED = "#7aa9c4"
app.configure(bg=BG)

title = ctk.CTkLabel(
    app, text="⚡ J.A.R.V.I.S Pro AI Assistant ⚡",
    font=("Consolas", 26, "bold"),
    text_color=NEON
)
title.pack(pady=10)


info_frame = ctk.CTkFrame(app, corner_radius=15, fg_color=BG)
info_frame.pack(pady=5, fill="x", padx=20)


time_label = ctk.CTkLabel(info_frame, text="Time: --:--", font=("Consolas", 14), text_color=TEXT)
time_label.grid(row=0, column=0, padx=20, pady=5)

cpu_label = ctk.CTkLabel(info_frame, text="CPU: --%", font=("Consolas", 14), text_color="lime")
cpu_label.grid(row=0, column=1, padx=20, pady=5)

ram_label = ctk.CTkLabel(info_frame, text="RAM: --%", font=("Consolas", 14), text_color="orange")
ram_label.grid(row=0, column=2, padx=20, pady=5)

weather_label = ctk.CTkLabel(info_frame, text="Weather: --", font=("Consolas", 14), text_color="magenta")
weather_label.grid(row=0, column=3, padx=20, pady=5)


button_frame = ctk.CTkFrame(app, corner_radius=15, fg_color=BG)
button_frame.pack(pady=10)

start_btn = ctk.CTkButton(button_frame, text="▶ Start Jarvis", command=start_jarvis, fg_color="green", hover_color="darkgreen")
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ctk.CTkButton(button_frame, text="⏹ Stop Jarvis", command=stop_jarvis, fg_color="red", hover_color="darkred")
stop_btn.grid(row=0, column=1, padx=10)


output_box = scrolledtext.ScrolledText(
    app, wrap=tk.WORD, width=110, height=18,
    font=("Consolas", 11), bg="black", fg="#39FF14", insertbackground="cyan"
)
output_box.pack(pady=10)


input_frame = ctk.CTkFrame(app, corner_radius=15, fg_color=BG)
input_frame.pack(pady=5)

input_box = ctk.CTkEntry(input_frame, placeholder_text="Type your command here...", width=450)
input_box.grid(row=0, column=0, padx=5)

def process_typed_command():
    global user_input_var
    command = input_box.get()
    input_box.delete(0, tk.END)

    if command.strip():
        if user_input_var is not None and user_input_var.get() == "":
            user_input_var.set(command.strip())
        else:
            safe_log(f"You (typed): {command}")
            task_queue.put(command.lower())

send_btn = ctk.CTkButton(input_frame, text="Send", command=process_typed_command, fg_color=NEON, hover_color="#00c7d9", text_color="black")
send_btn.grid(row=0, column=1, padx=5)


OPENWEATHER_API_KEY = "02a4cd0583fb56f43b0c97803d0e7f40"
CITY = "Mumbai"

def update_time():
    time_label.configure(text="Time: " + dt.datetime.now().strftime("%I:%M:%S %p"))
    app.after(1000, update_time)

def update_stats():
    cpu_label.configure(text=f"CPU: {psutil.cpu_percent()}%")
    ram_label.configure(text=f"RAM: {psutil.virtual_memory().percent}%")
    app.after(2000, update_stats)

def update_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        weather_label.configure(text=f"Weather: {temp}°C, {desc}")
    except:
        weather_label.configure(text="Weather: N/A")
    app.after(600000, update_weather)


update_time()
update_stats()
update_weather()
gui_update_loop()

app.mainloop()
