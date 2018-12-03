# 今日头条  街拍美女图  
# 待修改
# conding：utf-8
import requests

from bs4 import  BeautifulSoup
from urllib.parse import urlencode

import json

def get_page(offset):
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    data = {
        'offset': offset,
        'format':'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
    
    
if __name__ == '__main__':
    print(get_page(0))
