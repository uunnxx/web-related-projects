from urllib.request import urlopen
from urllib.error import HTTPError

import re

from bs4 import BeautifulSoup as BS

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs_object = BS(html)

# for child in bs_object.find('table', {'id': 'giftList'}).children:
#     print(child)


# for sibling in bs_object.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)


images = bs_object.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
    print(image['src'])
