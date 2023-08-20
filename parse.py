import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://hackathons.hackclub.com/'
req = requests.get(url)
soup = bs(req.text, "html.parser")
vacancies_names = soup.find_all('a')
for name in vacancies_names[0:-16]:
    if name.h3 is not None:
        if len(name.h3.contents) == 1 and name.span.contents[0] != 'In-Person':
            print(name.h3.contents[0], name['href'], name.footer.span.contents[0])