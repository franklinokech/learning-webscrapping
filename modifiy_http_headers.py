import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/usercheck/'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
                  'Safari/537.36 OPR/77.0.4054.80 '
    }

r = requests.get(url, headers=my_headers)

print(r.text)

# check request headers
print(r.request.headers)
