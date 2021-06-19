import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/redirect/'

# turn off redirects
r = requests.get(url, allow_redirects=False)

print(r.text)
print(r.headers['SECRET-CODE'])
