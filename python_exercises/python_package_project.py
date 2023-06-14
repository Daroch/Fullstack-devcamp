import requests
import inflection
import numpy as np
from bs4 import BeautifulSoup


def get_urls():
    url = 'https://api.dailysmarty.com/posts'
    r = requests.get(url)
    #soup = BeautifulSoup(r.json(), 'html.parser')
    #print(soup.find_all('url_for_post'))
    posts = r.json()['posts']
    for post in posts:
        endpoint = post['url_for_post'].rsplit('/', 1)[-1]
        print('"'+str(inflection.titleize(endpoint))+'"')
    
get_urls()
