#!/usr/bin/python3
import requests
import time
from stem import Signal
from stem.control import Controller
import os
from scraper_4 import vote
def new_ip():
    with Controller.from_port(port = 9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    return vote(proxies)

counter = 0
while (counter < 1024)
    os.system('sudo service tor restart')
    time.sleep(3);
    if new_ip() is True:
        counter += 1
