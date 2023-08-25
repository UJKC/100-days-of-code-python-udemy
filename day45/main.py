from bs4 import BeautifulSoup
import lxml

with open("day45\\website.html", encoding="utf8") as file:
    content = file.read()

Soup = BeautifulSoup(content, "lxml")

print(Soup.title)
print(Soup.title.name)
print(Soup.title.string)
print(Soup.a)
print(Soup.prettify())

all_anchor_tag = Soup.find_all(name="a")
print(all_anchor_tag)

for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))

heading = Soup.find(name="h1", id='name')
print(heading)
print(heading.getText())

heading_class = Soup.find(name="h3", class_="heading")
print(heading)
print(heading.getText())

selector = Soup.select(selector="p a")
print(selector)

for tag in selector:
    print(tag.get("href"))
    print(tag.string)