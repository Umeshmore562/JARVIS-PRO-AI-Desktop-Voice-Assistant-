⚡ JARVIS PRO – AI Desktop Voice Assistant  
Built using Python, CustomTkinter, Speech Recognition, and Intelligent Automation  

JARVIS PRO is an advanced AI-powered desktop assistant built with Python, combining  
✔ Voice Commands  
✔ Smart GUI  
✔ Email & WhatsApp Automation  
✔ Word & PPT Auto-Generator  
✔ Wikipedia/Google Integration  
✔ AI Text Generation  
✔ CPU/RAM Monitoring  
✔ Weather Updates  
✔ YouTube Search  
✔ Math Solver  
✔ Multithreading for Smooth Performance  

---

## 🖥️ **Demo Screenshot**
**<img width="1376" height="874" alt="Screenshot 2025-11-22 111146" src="https://github.com/user-attachments/assets/195d309a-202e-4da5-8da8-1bcd353eab74" />
**
<img width="1375" height="683" alt="Screenshot 2025-11-22 111231" src="https://github.com/user-attachments/assets/7199b58e-5eab-448f-9fc3-e5ea88bceb73" />

---

📁 Project Structure

```
Jarvis-AI/
│
├── main.py               
│
├── ai/
│   └── ai.py             
│
├── commands/
│   └── commands.py        
│
├── config/
│   └── config.py          
│
├── docs/
│   ├── create_word_doc.py 
│   └── create_ppt.py      
│
├── utils.py               
├── tts.py                
│
└── requirements.txt      
```
---

🚀 Features

🎙 Voice Interaction  
- Recognizes commands using SpeechRecognition
- Replies using pyttsx3 TTS

🪟 Elegant GUI  
Made using CustomTkinter, includes:
- Real-time CPU usage  
- RAM usage  
- Clock  
- Weather updates  
- Live logs  
- Input command box  

🌐 Internet Tasks  
- Google Search  
- YouTube Play  
- Wikipedia Summary  
- Open websites  

✉ Email & WhatsApp Automation  
- Email sending with contacts mapped in `config.py`
- WhatsApp messaging via pywhatkit

📄 Auto Document Creator  
- Word Document Generator (topic → ready content)
- PowerPoint Creator (topic → slide deck)

🧠 AI Text Generator  
- GPT4All Local model / OpenAI API (if enabled)

🧮 Math Solver  
- Handles spoken math queries  
Example: *"Calculate 40 plus 50 divided by 2"*

🌤 Weather  
Integrated using OpenWeather API

---

🛠 Installation

1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Jarvis-Pro-AI.git
cd Jarvis-Pro-AI
```
2️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

3️⃣ Add API Key  
Open `config/config.py` and edit:

```python
OPENWEATHER_API_KEY = "YOUR_KEY_HERE"
EMAIL_CONTACTS = {
    "dad": "example@gmail.com",
    "friend": "abc@gmail.com"
}
```

4️⃣ Run
```bash
python main.py
```

🧠 How It Works

🔹 Multithreading  
GUI stays smooth while:
- Voice engine runs separately  
- Commands process in background  
- Weather & stats update on timers  

🔹 Command Flow  
```
User Speaks → take_command() → process_command()  
→ Executes the correct module → Response displayed & spoken
```

🔹 Document Creation  
```
Topic → AI text generator → Word/PPT modules → Auto file saved
```

---

🧪 Example Commands

| Command | Action |
|--------|--------|
| “Play Believer” | Opens YouTube |
| “Send email to dad” | Triggers email module |
| “Create word on AI future” | Generates Word doc |
| “Search smartphones under 20k” | Google search |
| “Tell me a joke” | JARVIS tells a joke |
| “What is Python” | Wikipedia summary |
| “Calculate 55 divided by 5” | Math solver |
| “What’s the weather?” | Weather display |

---

📦 Requirements

(Already in requirements.txt)

```
pyttsx3
SpeechRecognition
pyaudio
pywhatkit
pyjokes
requests
wikipedia
python-docx
python-pptx
customtkinter
psutil
pyttsx3
gTTS
```

---

📝 License
This project is open-source under the MIT License.

---

❤️ Contribute
Pull requests are welcome!  
Feel free to add:
- More commands  
- Better UI  
- ChatGPT integration  
- More automation features
  
---

⭐ If you like the project, give it a star on GitHub!
