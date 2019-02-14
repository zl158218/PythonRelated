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

#########################################
## 爱问精选回答,所有问题爬取,并保存到MySQL##
#########################################

    
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
    url = 'https://iask.sina.com.cn/select/all.html'
    html = requests.get(url,headers=headers)
    
    if html.status_code == 200:
        soup = BeautifulSoup(html.text,'lxml')
        problem = soup.select('a[class="all-label-item"]')

        for i in problem:
            url_label = 'https://iask.sina.com.cn' + str(i['href'])
            child_tags = requests.get(url_label,headers=headers)

            if child_tags.status_code == 200:
                child_soup = BeautifulSoup(child_tags.text,'lxml')
                btn_max = child_soup.select('a[class="btn-max"]')

                for pages in btn_max:
                    if int(pages.get('p')) > 1:
                        max_page = int(pages.get('p'))
                        for  page in range(1,max_page):
                            all_url = 'https://iask.sina.com.cn' + str(i['href'][:37]) + '-' + str(page) + '.html'
                            # print(all_url)
                            all_date = requests.get(all_url,headers=headers)
                            if all_date.status_code == 200:
                                alls_soup = BeautifulSoup(all_date.text,'lxml')
                                problems = alls_soup.select('li  div[class="title fl"] a')
                                for iis in problems:
                                    sql = "insert into problems (problem) values(%s)"
                                    cur.execute(sql,(str(iis.text.strip())))
                                    conn.commit() # 提交数据
    cur.close() # 关闭游标
    print("save to mysql successful")

if __name__ == "__main__":
    problems()
