from flask import Flask

app = Flask(__name__)

# In terminal: set FLASH_APP=hello_flask.py

@app.route('/')
def hello():
    return "HI"

if __name__ == '__main__':
    app.run(debug=True)