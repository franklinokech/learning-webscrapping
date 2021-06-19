import requests


r = requests.get('https://api.github.com/user', auth=('github_user', 'github_pass'))
print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)

print(r.text)

print(r.json())
