from gpt4all import GPT4All
import threading
import os
from config import MODEL_PATH

gpt_lock = threading.Lock()
if not os.path.exists(MODEL_PATH):
    print("⚠️ GPT4All model not found!")

model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf", model_path=os.path.dirname(MODEL_PATH))

def ai_reply(prompt):
    with gpt_lock:
        with model.chat_session() as session:
            return session.generate(prompt, max_tokens=700)
