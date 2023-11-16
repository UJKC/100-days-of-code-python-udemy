from flask import Flask, render_template

app = Flask(__name__)

# In terminal: set FLASH_APP=hello_flask.py

@app.route('/')
def hello():
    return render_template('ide/index.html')

if __name__ == '__main__':
    app.run(debug=True)