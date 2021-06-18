import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'

r = requests.get(url)

# Which HTTP status did we get from the server?
print(r.status_code)

# What is the textual status code?
print(r.reason)

# What were the HTTP response headers?
print(r.headers)

# The request information is saved as python objects in r.request:
print(r.request)

# Whats were the HTTP request headers?
print(r.request.headers)

# The HTTP response content
print(r.text)

# The HTT request headers
print(r.re)