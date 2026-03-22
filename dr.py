import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import random
import webbrowser
import subprocess



# Logging configuration

LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"


os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[%(asctime)s ] %(name)s -%(levelname)s -%(message)s",
    level= logging.INFO 
)

#Activating voice system to our application

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150) 
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

#This is the function to speak the text

def speak(text):

    """This fuction converts text to speech and speaks it out loud
    args:
        text (str): The text to be spoken.
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()




#This function is to listen to the user's voice and convert it to text


def takeCommand():

    """This function listens to the user's voice and converts it to text using Google's speech recognition API.
    args:
        None
    returns:
        str: The recognized text from the user's voice input.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    

    return query    

def greeting():
    hour =( datetime.datetime.now().hour)
    
    if 0 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


speak(greeting())
speak("I am Dear, your virtual assistant. How can I assist you today?")

while True:

    query = takeCommand().lower()
    print(query)  
    
    if "your name" in query:
        speak("My name is Dear I am your virtual assistant.")
        logging.info("User asked for assistant's name.")    
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        logging.info("User asked for current time.")    
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print
        (results)
        speak(results)
        logging.info(f"User searched Wikipedia for: {query}")   
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")  
        logging.info("User asked to open YouTube.") 

    elif "open google" in query:
        webbrowser.open("https://www.google.com")  
        logging.info("User asked to open Google.")      

    elif "open linkedin" in query:
        webbrowser.open("https://www.linkedin.com")
        logging.info("User asked to open LinkedIn.")

    elif "open github" in query:
        webbrowser.open("https://www.github.com")
        logging.info("User asked to open GitHub.")

    elif "open facebook" in query:
        webbrowser.open("https://www.facebook.com")
        logging.info("User asked to open Facebook.")

    elif "open calendar" in query:
        webbrowser.open("https://calendar.google.com")
        logging.info("User asked to open Google Calendar.")

    elif "play music" in query:
        logging.info("User asked to play music.")
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
        else:
            speak("No music files found in the directory.")
    elif "open calculator" in query:
        subprocess.Popen("calc.exe")
        logging.info("User asked to open calculator.")
    elif "open notepad" in query:
        subprocess.Popen("notepad.exe")
        logging.info("User asked to open Notepad.")
    elif "open command prompt" in query:
        subprocess.Popen("cmd.exe") 
        logging.info("User asked to open Command Prompt.")
    elif "open camera" in query:
        subprocess.Popen("microsoft.windows.camera:")
        logging.info("User asked to open Camera.") 
    elif "how are you" in query:
        speak("I am doing well, thank you for asking! How can I assist you today?")
        logging.info("User asked how the assistant is doing.")
    elif"what can you do" in query:
        speak("I can assist you with various tasks such as opening applications, searching the web, providing information from Wikipedia, and much more. Just let me know what you need help with!")
        logging.info("User asked about the assistant's capabilities.")
    elif "who created you" in query:
        speak("I was created by Sanir Ahmed. I'm here to assist you with your tasks and make your life easier!")
        logging.info("User asked about the assistant's creator.")
    elif "joke" in query:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        joke = random.choice(jokes)
        speak(joke)
        logging.info("User asked for a joke.")

    elif "weather" in query:
        speak("I'm sorry, I don't have access to real-time weather information at the moment. However, you can check the weather on your preferred weather website or app.")
        logging.info("User asked for weather information.")
    elif "news" in query:
        webbrowser.open("https://news.google.com")  
        speak("Here are the latest news updates from Google News.") 
        logging.info("User asked for news updates.")
    elif "set a reminder" in query:
        speak("Sure, what would you like to be reminded about?")
        reminder = takeCommand().lower()
        speak(f"Reminder set for: {reminder}")
        logging.info(f"User set a reminder: {reminder}")
        google_reminder_url = f"https://www.google.com/calendar/render?action=TEMPLATE&text={reminder}"
        webbrowser.open(google_reminder_url)    
    elif "search" in query:
        speak("What would you like to search for?")
        search_query = takeCommand().lower()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        logging.info(f"User performed a web search for: {search_query}")
    elif "open email" in query:
        webbrowser.open("https://mail.google.com")
        logging.info("User asked to open email.")
    elif "open maps" in query:
        webbrowser.open("https://www.google.com/maps")
        logging.info("User asked to open Google Maps.")
    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        logging.info("User asked to open WhatsApp Web.")
    elif "take a note" in query:
        speak("What would you like to note down?")
        note_content = takeCommand().lower()
        with open("notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note_content}\n")
        speak("Note taken.")
        logging.info(f"User took a note: {note_content}")
    elif "show notes" in query:
        if os.path.exists("notes.txt"):
            with open("notes.txt", "r") as f:
                notes = f.read()
            speak("Here are your notes:")
            print(notes)    
            logging.info("User asked to show notes.")
        else:
            speak("You have no notes yet.")
            logging.info("User asked to show notes but no notes were found.")
    elif "clear notes" in query:
        if os.path.exists("notes.txt"):
            os.remove("notes.txt")
            speak("All notes have been cleared.")
            logging.info("User cleared all notes.")
        else:
            speak("You have no notes to clear.")
            logging.info("User asked to clear notes but no notes were found.")
    elif "open code" in query:
        code_path = "C:\\Users\\Sanir Ahmed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        if os.path.exists(code_path):
            os.startfile(code_path)
            logging.info("User asked to open Visual Studio Code.")
        else:
            speak("Visual Studio Code is not installed on this system.")
            logging.info("User asked to open Visual Studio Code but it was not found.")
    elif "play a movie" in query:
        search_query = query.replace("play a movie", "").strip()
        if search_query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}+full+movie")
            speak(f"Playing {search_query} on YouTube.")
            logging.info(f"User asked to play a movie: {search_query}")
    elif "open file explorer" in query:
        subprocess.Popen("explorer.exe")
        logging.info("User asked to open File Explorer.")

    elif "thanks" in query or "thank you" in query:
        speak("You're welcome! If you need any further assistance, feel free to ask.")
        logging.info("User expressed gratitude.")
    elif "goodbye" in query or "bye" in query:
        speak("Goodbye! Have a great day!")
        logging.info("User said goodbye.")
        break
    elif "stop" in query:
        speak("Goodbye! Have a great day!")
        logging.info("User asked to stop the application.")
        break
    elif "exit" in query:
        speak("Goodbye! Have a great day!")
        logging.info("User asked to exit the application.")
        break     
    

    else:
        speak("Sorry, I didn't understand that. Could you please repeat?")
        logging.info(f"User input not recognized: {query}")