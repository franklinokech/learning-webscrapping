import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r = requests.get(url)

html_content = r.text

html_soup = BeautifulSoup(html_content, 'html.parser')

episodes = []

ep_tables = html_soup.find_all('table', class_='wikiepisodetable')

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    # Start by fetching the header cells from the first row to determine the
    # Field names

    for head in table.find('tr').find_all('th'):
        headers.append(head.text)
    # Then go through the other rows except the first one
    for row in table.find_all('tr')[1:]:
        values = []

        for col in row.find_all(['th', 'td']):
            values.append(col.text)

        if values:
            episode_dict = {
                headers[i]: values[i] for i in range(len(values))
            }
            episodes.append(episode_dict)


# show result
for episode in episodes:
    print(episode)

