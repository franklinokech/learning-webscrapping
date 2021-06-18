import requests

url = 'http://www.webscrapingfordatascience.com/paramhttp/'

parameter = {
    'query': 'a query with /, spaces and?&'
}

r = requests.get(url, params=parameter)

print(r.url)
print(r.text)
