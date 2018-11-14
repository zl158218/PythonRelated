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
        authors = html.select('.aulink')[0] #获取作者，及作者链接
        author = authors.text   # 获取作者
        #print(author)
        author_url = authors.attrs['href']  # 获取作者链接
        #print(author_url)
        stick_time = html.select('a[style="color:#808080;cursor: initial; "]')[0] # 获取帖子发布时间
        #print(stick_time.text)
        reply = html.select('span[class="ansour box"]')[0]  # 获取帖子的回复及浏览数
        #print(reply.text)
        end_time = html.select('div[class="endreply box"] > a')[0]  # 最后回复时间
        #print(end_time.text)  
        end_author = html.select('div[class="endreply box"] > span')[0]  # 最后回复作者
        #print(end_author.text) 
        
        dicts = {
            'title': titles,
            'titles_url': titles_url,
            'author': author,
            'author_url': author_url,
            'stick_time': stick_time.text,
            'reply': reply.text,
            'end_time': end_time.text,
            'nd_author':end_author.text,
        }
        
        return dicts
      
        
def main():
    link = "https://bbs.hupu.com/lol"
    post_list = get_page(link)
    get_data(post_list,link)
  
    
if __name__ == '__main__':
    main()
