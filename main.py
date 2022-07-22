# anime recommnder time
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://myanimelist.net/animelist/Aaryaman0').text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
anime = soup.find_all('tbody', class_ = "list-item")
for item in anime:
    anime_name = item.text
    print(anime_name)