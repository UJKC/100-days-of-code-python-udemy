from bs4 import BeautifulSoup
import lxml

with open("day45\\website.html", encoding="utf8") as file:
    content = file.read()

Soup = BeautifulSoup(content, "lxml")

print(Soup.title)
print(Soup.title.name)
print(Soup.title.string)
print(Soup.a)