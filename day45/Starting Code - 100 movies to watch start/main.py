import urllib.request
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = urllib.request.urlopen(URL)
ujwal = response.read()

Soup = BeautifulSoup(ujwal, "lxml")
movies_list = Soup.find_all(name="h3", class_="title")
movies_list_reverse = movies_list[::-1]
movies_file_list = []

for movies in movies_list_reverse:
    print(movies.getText())
    movies_file_list.append(movies.getText() + "\n")

with open("day45\\Starting Code - 100 movies to watch start\\movies.txt", "w") as moviesfile:
    moviesfile.writelines(movies_file_list)
