from flask import Flask, render_template, request

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rule_based_chatbot import ChatBot
from training_data import validate_question

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


from pathlib import Path


@app.route('/respond', methods=['POST'])
def answer_user_question():
    print(os.path.dirname(__file__))
    aimls_dir = Path(r'../rule_based_chatbot/aimls')

    if aimls_dir.exists():
        os.chdir(r'../rule_based_chatbot/aimls')

    text = request.form['text']
    response = "Chatbot: " + ChatBot.from_ui(text)

    return response


from flask import jsonify


@app.route('/generate', methods=['GET'])
def generate_question():
    training_dir = Path(r'../training_data')

    if training_dir.exists():
        os.chdir(r'../training_data')

    return jsonify(validate_question.retrieve_questions())


@app.route('/validate', methods=['POST'])
def validate_response():
    user_answer = request.form["user_answer"]
    correct_answer = request.form["user_answer"]
    question = request.form["question"]

    response = is_answer_correct(user_answer, correct_answer, question)
    return jsonify(result=response)


def is_answer_correct(user_answer, correct_answer, question):
    # aici va fi apelata functia care va verifica raspunsul utilizatorului si va decide daca este sau nu corect
    return False


if __name__ == '__main__':
    app.run(debug=True)

# run with:
# export FLASK_APP=hello.py
#    flask run
