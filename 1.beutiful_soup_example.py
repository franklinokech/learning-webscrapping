import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=80255368'

r = requests.get(url)

html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'html.parser')

# print(html_soup.find('h1'))
#
# print(html_soup.find('', {'id': 'p-logo'}))
#
# for found in html_soup.find_all(['h1', 'h2']):
#     print(found)

# Find the first h1 tag

first_h1 = html_soup.find('h1')
# print(first_h1.name)  # h1

# print(first_h1.contents)

# print(str(first_h1))

# print(first_h1.text)

# print(first_h1.get_text())

# print(first_h1.attrs)

# print(first_h1['id'])

print('-----------------CITATIONS--------------')
cites = html_soup.find_all('cite', class_='citation', limit=5)

for citation in cites:
    print(citation.get_text())

    # Inside this cite element, find the first a tag
    link = citation.find('a')

    # Show its url
    print(link.get('href'))
    print()

