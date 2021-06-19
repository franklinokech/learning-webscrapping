import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/authentication/'

r = requests.get(url, auth=('myusername', 'mypassword'))

print(r.text)
print(r.request.headers)
