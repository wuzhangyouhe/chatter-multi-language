from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
import mandarin

amicia = ChatBot("Amica")
amicia.set_trainer(ListTrainer)
amicia.train(mandarin.mandarin_conversation)


print ("Amica: 李叔叔，今天中午您吃的是什么？")
while True:
    try:
        user_input = input("You: ")
        response = amicia.get_response(user_input).text
        print("Amica: " + response)
    except keyboardinterupt:
        break
