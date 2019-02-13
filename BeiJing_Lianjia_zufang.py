# 租房 爬取 https://bj.lianjia.com/zufang/
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql

def zufang(num):
    # 连接MySQL数据库
    conn = pymysql.connect(
        host = '192.168.19.128',
        user = 'root',
        passwd = '123qwe',
        db = 'LianJia'
    )
    cur = conn.cursor()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    
    url = 'https://bj.lianjia.com/zufang/pg' + str(num) + '/#contentList'
    # url = 'https://bj.lianjia.com/zufang/#contentList'
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text,'lxml')
        for number in range(len(soup.find_all(class_="content__list--item"))):
            title = soup.select('div[class="content__list"] p[class="content__list--item--title twoline"] a[target="_blank"]')[number].text.strip()
            # print("标题:",title)

            location = soup.select('p[class="content__list--item--des"]')[number]
            papers = ' '.join(location.text.replace("/"," ").strip().split())
            # print("简述:",papers)

            release_time = soup.select('p[class="content__list--item--time oneline"]')[number]
            # print(release_time.text)

            price = soup.select('span[class="content__list--item-price"]')[number]
            # print(price.text)
        
            sql = "insert into lianjia (title,location,release_time,price) values(%s,%s,%s,%s)"
            cur.execute(sql,(str(title),str(papers),str(release_time.text),str(price.text)))
            conn.commit() # 提交数据
    cur.close() # 关闭游标

if __name__ == "__main__":
    for num in range(1,20):
        zufang(num)
    print("save to MySQL ok")

# truncate table tablename ; 清空表内容,保留表结构.
