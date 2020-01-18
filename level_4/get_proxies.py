#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs

def get_proxies():
    url = 'https://free-proxy-list.net/'
    res = requests.get(url)
    soup = bs(res.content, features="html5lib")
    dirs  = soup.findAll('td')[::8]
    ports = soup.findAll('td')[1::8]
    proxies = list(zip(map(lambda x: x.text, dirs), map(lambda x: x.text, ports)))[:20]
    proxies = list(map(lambda x: {'https': x[0] + ':' + x[1]}, proxies))
    
    print(proxies)
    return proxies



