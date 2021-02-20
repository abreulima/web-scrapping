import requests
from bs4 import BeautifulSoup

url = "https://abreulima.github.io/web-scrapping/"

source = requests.get(url).content

soup = BeautifulSoup(source, features="html.parser")

main_title = soup.find(id="main-title")

print(main_title)
