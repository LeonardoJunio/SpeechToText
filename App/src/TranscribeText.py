import speech_recognition as sr

class TranscribeText():
    
    def __init__(self):
        r = sr.Recognizer()

        music = sr.AudioFile("files/music_wav.wav")
        with music as source:
            audio = r.record(source)
            
        print("Transcribing...")

        try:
            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    