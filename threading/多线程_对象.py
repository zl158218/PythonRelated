# coding:utf-8
# 多线程 对象

import requests
from bs4 import BeautifulSoup
import threading

def problems(headers,page):
    # for page in range(1,3):
    url = 'https://iask.sina.com.cn/select/list/582a7a0ce4b0b20e39853085-' + str(page) + '.html'
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text,'lxml')
        problem = soup.select('li  div[class="title fl"] a')
        for i in problem:
            print(i.text.strip())
            print()

def main():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # 一个线程
    t1 = threading.Thread(target=problems,args=(headers,4,))   # 添加一个线程
    t1.start()   
    t1.join()
    print('-------单--线--程--结--束-------')
    print()                                       

    # 多个线程
    for i in range(30,40,3):
        t = threading.Thread(target=problems,args=(headers,i,))
        t.start()
        print(t.is_alive()) # 查看状态
        t.join()

if __name__ == "__main__":
    main()
