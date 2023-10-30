#!/usr/bin/python3
# Imports
import subprocess

try:
    import speech_recognition as sr
except ImportError:
    print("speech_recognition library not found. Installing...")
    subprocess.check_call(["pip", "install", "speech_recognition"])
    import speech_recognition as sr

try:
    import os
except ImportError:
    print("os library not found. Installing...")
    subprocess.check_call(["pip", "install", "os"])
    import os


# Open/Close
def command(voic):
    com=voic.split()
    try:
        if com[0]=="open"   :
            subprocess.Popen([com[1].lower()])
        elif com[0]=='close':
            os.system(f"killall -9 {com[1].lower()}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    recognation()

# Recognation/Speak commands
def recognation():
    with sr.Microphone() as mic:
            recognize=sr.Recognizer()
            recognize.adjust_for_ambient_noise(mic)
            print("Please tell  open or close(open Firefox) or break") 
            audio=recognize.listen(mic)
    
    text = recognize.recognize_google(audio)
    print(text)
    if not text.lower()=="break":
        command(text)
        

def main():
    recognation() 
    
main()