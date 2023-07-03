import pyttsx3

def readText(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine
