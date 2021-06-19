import re
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)

html_content = r.text

html_soup = BeautifulSoup(html_content, 'html.parser')

# find tags starting with letter h
print(html_soup.find(re.compile('^h')))
