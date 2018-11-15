''' --------目标：--------
    帖子名称
    帖子链接
    作者
    作者链接
    创建时间
    回复数
    浏览数
    最后回复时间
    最后回复用户
####### 待修改 ########
    1,动态 Cookies
    2,存入mysql
    3,存入mongodb
    4,存入redis  
'''

# coding:utf-8
import requests
from bs4 import BeautifulSoup
import datetime
from lxml import etree
import re


def get_page(link):
    # 技术有限，先用静态Cookies
    # 获取页面html
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Cookie': '_cnzz_CV30020080=buzi_cookie%7Cec37a3af.2c7b.efb6.8885.07033824b4d7%7C-1; _dacevid3=ec37a3af.2c7b.efb6.8885.07033824b4d7; __gads=ID=0a83550d3fac9e34:T=1541944038:S=ALNI_Ma9uJvL88LfvYAquEdy03bg_BAFUA; _HUPUSSOID=2076175d-d05f-4c4e-925c-c0b842c1f488; _cnzz_CV30020080=buzi_cookie%7Cec37a3af.2c7b.efb6.8885.07033824b4d7%7C-1; PHPSESSID=1as5ef0c6fcqgfenmv2q1gp4q0; _CLT=918ebe7bb324d8673460f7af1d701a5c; u=41278725|TWlu6LWw6aOO|c408|f43026cbf7c1fe81c2609446a5bceb6f|f7c1fe81c2609446|aHVwdV82OGE2ZDkyYzA0N2YzNGFi; us=7a1d1fc9f23860ba2a4e221634c3c1c0e49f55f5d0d2cebd239cd2938bc5051a48bcb1b04b7f1f01339ae2a92fcf868d06fdd121c20f685de7567e544793017f; ua=59318616; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1541946457,1542196594,1542284061; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1542288500; _fmdata=NNYtSOYHBMOr0wruyOjfhZ9%2B00dqiFEAQ8pKfpTyBGbX6xYDD4VQNEGRTBSvGa70G97xjW1%2Bz%2BjBvQfk3Dr8EBZ9CHkqTd9sYqgM9HX4Uv0%3D; __dacevst=5b23c262.7cff1a08|1542290409096'

    }
    r = requests.get(link, headers=headers)
    html = r.content
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_data(post_list, link):
    '''获取内容'''
    post = post_list.select('.for-list li')
    # print(post)

    lists = []
    for html in post:
        title = html.select('.truetit')[0]
        titles = title.text  # 文章标题
        # print(titles)
        titles_urls = title.attrs['href']  # 获取文章url
        titles_url = "https://bbs.hupu.com/" + titles_urls  # 拼接文章 url
        # print(titles_url)
        authors = html.select('.aulink')[0]  # 获取作者，及作者链接
        author = authors.text  # 获取作者
        # print(author)
        author_url = authors.attrs['href']  # 获取作者链接
        # print(author_url)
        stick_time = html.select('a[style="color:#808080;cursor: initial; "]')[0]  # 获取帖子发布时间
        # print(stick_time.text)
        reply = html.select('span[class="ansour box"]')[0]  # 获取帖子的回复及浏览数
        # print(reply.text)
        replys = "".join(reply.text.split())     # 去除空格nbsp or "\xa0" 字符串，
       
        end_time = html.select('div[class="endreply box"] > a')[0]  # 最后回复时间
        # print(end_time.text)
        end_author = html.select('div[class="endreply box"] > span')[0]  # 最后回复作者
        # print(end_author.text)
        # 获取的字段生成到 list
        lists.append(
            [titles, titles_url, author, author_url, stick_time.text, replys, end_time.text, end_author.text])

    return lists

def save_to_mysql():
    pass


def main():
    for nums in range(0,101):
        link = "https://bbs.hupu.com/lol-" + str(nums)   #拼接url地址
        post_list = get_page(link)
        lists = get_data(post_list,link)
        for l in lists:
            print(l)
            #print(nums)

if __name__ == '__main__':
    main()






