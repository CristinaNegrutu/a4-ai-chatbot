from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, AI!'

# run with:
#	export FLASK_APP=hello.py
#       flask run
