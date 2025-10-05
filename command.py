from datetime import datetime,date
import psutil
import os
import subprocess
import signal
import webbrowser
from speak import speak
from example import example
from tempCodeRunnerFile import wordout
def process(c):
    if "motivate" in c.lower():
        a=wordout()
        speak(a)
    elif("open google") in c.lower():
        webbrowser.open("https://www.google.co.uk/")
    elif("open youtube") in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif("open whatsapp") in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "close google" in c.lower():
        speak("Closing the Google")
        os.system("taskkill /f /im chrome.exe")
    elif "sleep" in c:
        speak("Sleeping for now. bye sir !")
    elif "work" in c.lower() or "work" in c.lower():
        speak("showing the task")
        print("showing the task")
        import subprocess
        subprocess.call(["python", "la.py"])
        speak("updated the task sir")
    elif "question" in c.lower() or "explain" in c.lower() or "doubt" in c.lower:
        speak("I can open gemini or gpt to solve your queries ")
        speak("which one you want master")
        from aibaat import aiki
        aiki()
    
   
    else:
        speak("didn't understand master")
