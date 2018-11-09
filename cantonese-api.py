from flask import Flask, jsonify, request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
from flask_cors import CORS
import cantonese
app = Flask(__name__)
CORS(app)

amicia = ChatBot("Amica")
amicia.set_trainer(ListTrainer)
amicia.train(cantonese.cantonese_conversation)

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
