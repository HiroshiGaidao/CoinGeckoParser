import time

import requests
from bs4 import BeautifulSoup

def pars():
    url = 'https://www.coingecko.com/en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('tr')
    i=0
    dataset = []
    for item in items:
        if i < 65:
            if item.find('a', class_="tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between") is not None:
                name = item.find('a', class_="tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between").text
                cost = item.find('span', class_="no-wrap").text
                i+=1
                add = [i, name.split('\n')[1], cost]
                dataset.append(add)
        else:
            pass
    return dataset, time.asctime()
