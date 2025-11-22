import smtplib
from email.message import EmailMessage
import re
from config import SENDER_EMAIL, SENDER_PASSWORD, EMAIL_CONTACTS
from tts import speak
import wikipedia


def send_email_interactive(name, log_func=None, typed_input_func=None):
    from utils import take_command

    to_email = EMAIL_CONTACTS.get(name)
    if not to_email:
        speak(f"No email found for {name}", log_func)
        return

    
    speak("What is the subject?", log_func)
    subject = typed_input_func() if typed_input_func else take_command()

    
    speak("What do you want to send?", log_func)
    body = typed_input_func() if typed_input_func else take_command()

    send_email(to_email, subject, body, log_func)


def send_email(to_email, subject, body, log_func=None):
    """Actually sends the email using SMTP"""
    try:
        msg = EmailMessage()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        speak(f"Email sent to {to_email}", log_func)
    except Exception as e:
        speak(f"Failed to send email: {e}", log_func)


def solve_math(query, log_func=None):
    try:
        q = query.lower().replace("calculate", "").replace("what is", "").strip()
        q = q.replace("plus", "+").replace("minus", "-")
        q = q.replace("into", "*").replace("multiplied by", "*")
        q = q.replace("divided by", "/")
        q = q.replace("times", "*").replace("x", "*")
        q = q.replace("power", "**")

        q = re.sub(r'[a-zA-Z]', '', q).strip()

        if not re.match(r'^[0-9+\-*/(). ]+$', q):
            msg = "Sorry, I could not understand the math problem."
            speak(msg, log_func)
            return None

        result = eval(q)
        msg = f"The answer is {result}"
        speak(msg, log_func)   
        return result

    except Exception as e:
        msg = f"Sorry, I could not calculate that. Error: {e}"
        speak(msg, log_func)  
        return None



def wiki_search(query, log_func=None):
    """Fetch short summary from Wikipedia with fuzzy matching."""
    try:
        
        query = query.lower().replace("who is", "").replace("what is", "").replace("tell me about", "").strip()

        
        results = wikipedia.search(query)
        if not results:
            msg = "Sorry, I couldn't find anything on that."
            speak(msg, log_func)
            if log_func: log_func(msg)
            return None

        
        topic = results[0]
        info = wikipedia.summary(topic, sentences=2)

        speak(info, log_func)
        return info

    except Exception as e:
        msg = "Sorry, I couldn't fetch information right now."
        speak(msg, log_func)
        if log_func: log_func(f"{msg} (Error: {e})")
        return None

