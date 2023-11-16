from flask import Flask
from random import randint

app = Flask(__name__)

int_var = randint(0,2)
print(int_var)

# In terminal: set FLASH_APP=hello_flask.py

def validate(var, int_var):
    if (int_var == var):
        return '<iframe src="https://giphy.com/embed/X8RSwd1089xDvOjQnT" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    else:
        return '<iframe src="https://giphy.com/embed/wqdK9as8onGrMZDUW8" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'

@app.route('/')
def hello():
    return '<iframe src="https://giphy.com/embed/RxTd2Dkeldzlh3Q5F6" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'

@app.route('/guess/<var>')
def guessed(var):
    return validate(int(var), int_var)

if __name__ == '__main__':
    app.run(debug=True)