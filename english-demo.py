from flask import Flask, jsonify, request
from flask_cors import CORS
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import english
import json

app = Flask(__name__)
CORS(app)

amicia = ChatBot("Amicia")
amicia.set_trainer(ListTrainer)
amicia.train(english.english_conversation)

@app.route("/conversation", methods=['POST'])

def conversation():
    user_input = request.get_json()
    print (user_input)
    question = user_input['question']
    response = amicia.get_response(question).text
    print(response)
    output = { 'data': response }
    return json.dumps(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5080')
