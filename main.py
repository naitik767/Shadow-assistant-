from playsound import playsound
import sounddevice as sd
import vosk
import queue 
import json
import speech_recognition as sr
import pyttsx3
from datetime import datetime,date
import psutil
import os
import subprocess
import signal
import webbrowser
from listenmodule import listen_command
from command import process
from speak import speak
from detect import detect_wake_word    
import time
speak("say shadow to activate")
print("say shadow to activate")
while True:
    if detect_wake_word():
        speak("yes master ")
        time.sleep(1)
        listen_command()
        
    sd.sleep(500)