from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(0, 11)
    todays_year = datetime.now()
    todays_year_year = todays_year.year
    return render_template('index.html', num=random_number, year = todays_year_year)

@app.route('/guess/<name>')
def guesser(name):
    # Print the name parameter first
    print(name)

    # Construct the API URL
    url = f"https://api.genderize.io?name={name}"

    # Make the API request
    gender_data = requests.get(url=url)

    # Check if the request was successful (status code 200)
    if gender_data.status_code == 200:
        # Parse the JSON response
        gender_data = gender_data.json()

        # Extract data from the JSON response
        name = gender_data.get('name')
        gender = gender_data.get('gender')

        # Render the template with the obtained data
        return render_template('guess.html', name=name, gender=gender)
    else:
        # Handle the case where the API request was not successful
        print(f"API request failed with status code: {gender_data.status_code}")
        return render_template('error.html', message='Failed to retrieve data from the API')
    
@app.route('/blog')
def bloger():

    # Construct the API URL
    url = "https://api.npoint.io/c790b4d5cab58020d391"

    # Make the API request
    blog_data = requests.get(url=url)

    # Check if the request was successful (status code 200)
    if blog_data.status_code == 200:
        # Parse the JSON response
        blog_data = blog_data.json()

        # Render the template with the obtained data
        return render_template('blog.html', blog=blog_data)
    else:
        # Handle the case where the API request was not successful
        print(f"API request failed with status code: {blog_data.status_code}")
        return render_template('blog.html', message='Failed to retrieve data from the API')

if __name__ == "__main__":
    app.run(debug=True)


