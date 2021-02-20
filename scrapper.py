import requests
from bs4 import BeautifulSoup

url = "https://abreulima.github.io/web-scrapping/"
source = requests.get(url).content
soup = BeautifulSoup(source, features="html.parser")

headline = soup.find(id="main-title")
print(f"The headline is {headline.text}.")

team_ul = soup.find("ul")
team_list = team_ul.find_all("li")

for person in team_list:
    print(person.text)

products = soup.find_all(class_="price")

for p in products:
    name = p.find("h2")
    price = p.find("p")
    print(name.text, price.text)

item = soup.find(attrs={"status": "10 Def"})
print(f"The item that has 10 Def is {item.text}")