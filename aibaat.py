import webbrowser
from speak import speak
def aiki():
        from listenmodule import listen_command1
        print("say")
        
        l =listen_command1()
       
        if "google" in l.lower():
            webbrowser.open("https://gemini.google.com/app") 
            speak("opening gemini for you master")
        elif "chat" in l.lower():
            webbrowser.open("https://chatgpt.com/?model=auto")
            speak("opening gpt for you master ")
        else:
            speak("i didn't understand master")
            speak ("please repeat master")
            aiki()