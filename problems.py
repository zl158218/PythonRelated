# 爱问 问题爬取,保存到数据库
import requests
from bs4 import BeautifulSoup
import pymysql

def problems():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    conn = pymysql.connect(
        host = '192.168.19.128',
        user = 'root',
        passwd = '123qwe',
        db = 'test'
    )
    cur = conn.cursor()
    for page in range(1,10):
        url = 'https://iask.sina.com.cn/select/list/582a7a0ce4b0b20e39853085-' + str(page) + '.html'
        html = requests.get(url,headers=headers)
        if html.status_code == 200:
            soup = BeautifulSoup(html.text,'lxml')
            problem = soup.select('li  div[class="title fl"] a')
            for i in problem:
                sql = "insert into problems (problem) values(%s)"
                cur.execute(sql,(str(i.text.strip())))
                conn.commit() # 提交数据
    cur.close() # 关闭游标
    print("save to mysql successful")
    
if __name__ == "__main__":
    problems()
