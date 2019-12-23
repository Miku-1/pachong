# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月22日 上午11:35
    @File   : test.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import requests
from lxml import etree
import urllib.parse

def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    url = 'https://live.kuaishou.com/u/3xvyedqvk5vtv4k/3x8fcqae8yvpju9?'
    response = requests.get(url=url, headers=headers).text
    return response
url = 'https://live.kuaishou.com/v/hot'

response = get_response(url)
print(response)
