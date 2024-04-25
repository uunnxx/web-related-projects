import requests
from bs4 import BeautifulSoup as bs


HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


URI = 'https://realpython.com/search?kind=article&kind=course&order=newest'
session = requests.Session()

try:
    req = session.get(URI, headers=HEADERS)
except Exception:
    print('error occurred')


soup = bs(req.content, 'html.parser')
# rows = soup.find('div', attrs={'class': 'container my-3'})
rows = soup.find('div', attrs={'class': 'my-0 h5'})

print(rows)

