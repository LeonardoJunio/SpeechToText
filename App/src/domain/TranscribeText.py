import speech_recognition as sr
from src.auxiliaries.constants.Constants import *

class TranscribeText:

    def __init__(self):
        TranscribeText.trasncribeAudioFromFile(Constants.MUSIC_FILE)

    def trasncribeAudioFromFile(fileName: str):
        r = sr.Recognizer()

        music = sr.AudioFile(fileName)
        
        with music as source:
            audio = r.record(source)

        print("Transcribing...")

        try:
            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
