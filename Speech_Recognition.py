#!/usr/bin/python3

# Imports
import subprocess
import os
try:
    import speech_recognition as sr
except ImportError:
    print("Speech Recognition library not found. Installing...")
    subprocess.check_call(["pip", "install", "speech_recognition"])
    import speech_recognition as sr

# Constants
OPEN_COMMAND = "open"
CLOSE_COMMAND = "close"

# Open/Close
def command(voic):
    com = voic.split()
    try:
        if com[0] == OPEN_COMMAND:
            subprocess.Popen([com[1].lower()])
        elif com[0] == CLOSE_COMMAND:
            os.system(f"killall -9 {com[1].lower()}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio.")
    except sr.RequestError as error:
        print(f"Could not request results from Google Web Speech API: {error}")
    recognation()

# Recognition/Speak commands
def recognition():
    with sr.Microphone() as mic:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(mic)
        print("Please say 'open' or 'close' (e.g., 'open Firefox') or 'break' to exit.")
        audio = recognizer.listen(mic)

    text = recognizer.recognize_google(audio)
    print(f"Recognized command: {text}")
    if not text.lower() == "break":
        command(text)

def main():
    recognition()

if __name__ == "__main__":
    main()
