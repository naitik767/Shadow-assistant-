import sounddevice as sd
import speech_recognition as sr
from speak import speak
from command import process

def listen_command():
     r=sr.Recognizer()
     with sr.Microphone()as source:
         speak("tell me the command sir")
         print("speak now")
         r.adjust_for_ambient_noise(source,duration=1)
         
         try:
            audio = r.listen(source,timeout=5)
            command=r.recognize_google(audio)
            
            print(" you said ", command )
            speak(f" you said  {command}")
            process(command) 
         except:
            speak("couldn't understand")
            listen_command()
def listen_command1():
     t=sr.Recognizer()
     with sr.Microphone()as source:
         
         print("speak now")
         t.adjust_for_ambient_noise(source,duration=1)
         
         try:
            audio = t.listen(source,timeout=5)
            command=t.recognize_google(audio)
            print(command)
            return command
         
         except:
            speak("repeat please")
            listen_command1()
