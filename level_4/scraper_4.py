#!/usr/bin/python3
import mechanize
import pytesseract
from bs4 import BeautifulSoup as bs
from subprocess import check_output
from itertools import cycle

import traceback
import requests
import json

def vote(proxy):
    try:
        print('opening site')
        url = "http://158.69.76.135/"
        #br.set_proxies(proxy)
        ur = url + "level4.php"
        print('site opened')
        session = requests.Session()
        response = session.get(ur, proxies=proxy)
        #print(response.text)
        soup = bs(response.text, "html.parser")
        key_tag = soup.find(attrs={"name": "key"})
        value = key_tag.get("value")
        print("key: ", value)
        values = {'id': '1305', 'holdthedoor': 'Submit', 'key': str(value)}
        response = session.post(ur, data=values, proxies=proxy, headers={'Referer': ur})
        re = response.content
        if re == "You already voted today [12]":
            print(re)
            state = False
        else:
            print(re[:80])
            state = True
        return state

    except Exception as e:
        print(e)
        return False
