from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
import cantonese

amicia = ChatBot("Amica")
amicia.set_trainer(ListTrainer)
amicia.train(cantonese.cantonese_conversation)

print ("Amicia: Uncle李，食咗早餐未")
while True:
    try:
        user_input = input("You: ")
        response = amicia.get_response(user_input).text
        print("Amica: " + response)
    except keyboardinterupt:
        break
