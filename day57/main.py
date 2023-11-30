from flask import Flask, render_template
from random import randint
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(0, 11)
    todays_year = datetime.now()
    todays_year_year = todays_year.year
    return render_template('index.html', num=random_number, year = todays_year_year)


if __name__ == "__main__":
    app.run(debug=True)


