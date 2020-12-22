import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[19].id)
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            print(voice)
            command = listener.recognize_google(voice, language="es-ES")
            command = command.lower()
            print(command)
            if 'ok linux' in command:
                command = command.replace('ok linux', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'youtube' in command:
        song = command.replace('youtube', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'hora' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Son las: ' + time)
    elif 'wikipedia' in command:
        article = command.replace('busca en wikipedia', '')
        article = article.replace('wikipedia', '')
        info = wikipedia.summary(article, 1)
        talk(info)
    elif 'chiste' in command:
        talk(pyjokes.get_joke('es'))


run_alexa()
