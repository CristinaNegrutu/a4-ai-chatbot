from flask import Flask, render_template, request

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rule_based_chatbot import ChatBot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/respond', methods=['POST'])
def form_post():
    print(os.path.dirname(__file__))
    from pathlib import Path
    aimls_dir = Path(r'../rule_based_chatbot/aimls')

    if aimls_dir.exists():
        os.chdir(r'../rule_based_chatbot/aimls')

    text = request.form['text']
    response = "Chatbot: " + ChatBot.from_ui(text)

    return response

if __name__ == '__main__':
    app.run(debug=True)

# run with:
# export FLASK_APP=hello.py
#    flask run
