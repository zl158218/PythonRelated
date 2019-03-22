# coding:utf-8
# 多线程: 继承, 加锁

import requests
from bs4 import BeautifulSoup
import threading

threadLock = threading.Lock()
def problems(page):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # for page in range(1,3):
    url = 'https://iask.sina.com.cn/select/list/582a7a0ce4b0b20e39853085-' + str(page) + '.html'
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text,'lxml')
        problem = soup.select('li  div[class="title fl"] a')

        for i in problem:
            print(i.text.strip())
            print()

class MyThread(threading.Thread):
   
    def __init__(self,headers,page):
        threading.Thread.__init__(self)
        self.page = page
        self.headers = headers

    def run(self):
        print("运行problem，end。。。")
        # print(self.page)
        # 加锁
        threadLock.acquire()
        print("start...  ")
        print(self.page)
        problems(self.page)
        # 释放锁，开启下一个线程
        threadLock.release()

def main():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    threads = []
    for page in range(10):
        print("start...  ")
        t = MyThread(headers,page)
        threads.append(t)
        print(page)

    for t in threads:
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
