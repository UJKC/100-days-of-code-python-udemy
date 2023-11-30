from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

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

@app.route('/blog/post/<num>')
def bloger(num):

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
