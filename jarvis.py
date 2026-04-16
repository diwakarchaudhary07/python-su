import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import pyautogui

# --- Voice Setup ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# 0 male ke liye, 1 female ke liye (Aap change karke check kar sakte hain)
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 180) # Bolne ki speed

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        # Shor saaf karne ke liye
        listener.adjust_for_ambient_noise(source, duration=0.5)
        print("\nSuni taani... Boliye... (Listening...)")
        voice = listener.listen(source)

    try:
        # language='hi-IN' Bhojpuri aur Hindi dono ke liye best kaam karta hai
        command = listener.recognize_google(voice, language='hi-IN')
        command = command.lower()
        print(f"Aapne kaha: {command}")
        return command
    except:
        return ""

def run_assistant():
    command = take_command()
    
    if not command:
        return True

    # --- Entertainment (Gaana) ---
    if 'बजाओ' in command or 'baja' in command or 'play' in command:
        song = command.replace('play', '').replace('baja', '').replace('बजाओ', '')
        speak(f'Theek ba, YouTube par {song} bajawat tani.')
        pywhatkit.playonyt(song)

    # --- App Opening ---
    elif 'खोल' in command or 'open' in command or 'kholo' in command:
        if 'notepad' in command:
            speak('Notepad khul gail.')
            os.system('notepad')
        elif 'calculator' in command:
            speak('Calculator khol tani.')
            os.system('calc')
        elif 'chrome' in command:
            speak('Chrome khul gail ba.')
            os.system('start chrome')

    # --- Window Controls (Minimize/Close) ---
    elif 'छोटा' in command or 'minimize' in command or 'desktop' in command:
        speak('Theek ba, sab minimize kar tani.')
        pyautogui.hotkey('win', 'd') # Desktop show karega

    elif 'बंद' in command or 'close' in command:
        speak('Window band kar tani.')
        pyautogui.hotkey('alt', 'f4') # Current window close karega

    # --- Time ---
    elif 'समय' in command or 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'Abhi ke time ho rahal ba {time}')

    # --- Exit ---
    elif 'बंद हो' in command or 'exit' in command or 'stop' in command:
        speak('Pranam Diwakar, fir milab!')
        return False
    
    else:
        speak('Humra samajh me nahi aayil, fir se boli.')
    
    return True

# --- Program Start ---
if __name__ == "__main__":
    speak("Pranam Diwakar, batai ka sahayata kari?")
    while True:
        if not run_assistant():
            break