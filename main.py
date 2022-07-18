# anime recommnder time
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://myanimelist.net/animelist/Aaryaman0').text
print(html_text)

soup = BeautifulSoup(html_text, 'lxml')