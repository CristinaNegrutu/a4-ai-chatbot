from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    print(text)
    return "Bot: I don't know the answer!"


if __name__ == '__main__':
    app.run(debug=True)

# run with:
#	export FLASK_APP=hello.py
#       flask run
