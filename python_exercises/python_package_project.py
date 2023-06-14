import requests
import inflection
import numpy as np
from bs4 import BeautifulSoup


def get_urls():
    url = 'https://dailysmarty.com/posts'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all(attrs={"data-turbolinks": "false"})
    for link in links:
        endpoint = link['href'].rsplit('/', 1)[-1]
        print('"'+str(inflection.titleize(endpoint))+'"')
    
get_urls()
