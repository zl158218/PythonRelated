#  虎扑步行街   lol 板块爬取
'''目标：
        帖子名称
        帖子链接
        作者
        作者链接
        创建时间
        回复数
        浏览数
        最后回复用户
        最后回复时间
        网页地址
'''


import requests
from bs4 import BeautifulSoup
import datetime
from lxml import etree
import re
def get_page(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    r = requests.get(link,headers=headers)
    html = r.content
    html = html.decode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    return soup
        
def get_data(post_list,link):
    post = post_list.select('.for-list li')
    #print(post)
    for html in post:
        title = html.select('.truetit')[0]   
        titles = title.text   # 文章标题
        #print(titles)
        titles_urls = title.attrs['href'] # 获取文章url
        titles_url = "https://bbs.hupu.com/" + titles_urls  # 拼接文章 url
        #print(titles_url)
        
            
            
def main():
    link = "https://bbs.hupu.com/lol"
    post_list = get_page(link)
    get_data(post_list,link)
if __name__ == '__main__':
    main()
