from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

import re


html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs_object = BS(html)

for link in bs_object.find('div', {'id': 'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')
):
    if 'href' in link.attrs:
        print(link.attrs['href'])


# for link in bs_object.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
