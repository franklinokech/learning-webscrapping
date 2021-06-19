import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/referercheck/secret.php'

# Spoof the referer
my_headers = {
    'Referer': 'http://www.webscrapingfordatascience.com/referercheck/'
}

r = requests.get(url, headers=my_headers)

print(r.text)
