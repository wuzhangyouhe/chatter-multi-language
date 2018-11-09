import speech_recognition as sr
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from datetime import datetime, time
import english

def setup():
    chatbot = ChatBot('Amica')

    chatbot.set_trainer(ListTrainer)
    chatbot.train(english.english_conversation)
    while True:
        print("starting to speak ...")
        now = datetime.now()
        beginning_of_day = datetime.combine(now.date(), time(0))
        print ((now - beginning_of_day).seconds)
        get_response(chatbot)

def get_response(chatbot):
    # Get a response to an input statement
    speech = return_audio()
    print (chatbot.get_response(speech))

def return_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio)
        try:
            print (str(speech))
            return speech
        except TypeError:
            print ("Error! Could not convert speech to string!")
    except sr.UnknownValueError:
        print ("Error! Could not process that audio.")
        return "Error!"
    except sr.RequestError as e:
        print ("Error! No internet connection to Google Sound Recognizer.")
        return "Error!"

setup()
