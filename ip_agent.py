# coding:utf-8
import requests
import re
import random
import time

def get_ip():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    for i in range(1, 10):
        url = 'https://www.xicidaili.com/nn/' + str(i)  # 国内高匿代理IP
        # proxies = {'https': 'https://116.209.56.176:9999'}   # ip失效了,自行更换
        html = requests.get(url, headers=headers,proxies=proxies).text
        pattern = re.compile('<td>([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)</td>.*?<td>(\d*?)</td>.*?<td>([A-Z]*)</td>', re.S)
        ips = pattern.findall(html)
        for ip in ips:
            if str(ip[2]) == "HTTPS":
                try:
                    proxies = {'https': 'https://' + ip[0] + ":" + ip[1]}
                    url = 'https://www.163.com/'
                    douban = requests.get(url, headers=headers, proxies=proxies, timeout=1)
                    if douban.status_code == 200:
                        return proxies
                except:
                    continue

if __name__ == "__main__":
    get_ip()
    #xx = get_ip()
    #print(xx)
###########################################
#  多线程
###########################################
import threading
import requests
import time
import random
import re

class Crawl(threading.Thread):
    base_url = 'http://hr.tencent.com/position.php?start=%d'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    def __init__(self,i):
        super(Crawl, self).__init__()
        self.i = i

    def run(self):
        ip = self.getPage(self.i)
        return ip

    def getPage(self,i):
        if str(i[2]) == "HTTPS":
            try:
                proxies = {'https': 'https://' + i[0]+ ":" + i[1]}
                print("测试：",proxies)
                url = 'https://www.163.com/'
                html = requests.get(url, headers=headers, proxies=proxies, timeout=1)
                if html.status_code == 200:
                    print("可用代理：",proxies)
                    return proxies
            except:
                return None

def get_ip(headers):
    ip_list = []
    for page in range(2,10,int(random.choice(range(1,4)))):
        url = 'https://www.xicidaili.com/nn/' + str(page)  # 国内高匿代理IP
        # proxies = {'https': 'https://210.5.10.87:53281'}
        html = requests.get(url, headers=headers,verify=False).text
        pattern = re.compile('<td>([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)</td>.*?<td>(\d*?)</td>.*?<td>([A-Z]*)</td>', re.S)
        ips = pattern.findall(html)
        ip_list = ip_list + ips
    return ip_list

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    print(time.ctime())
    ip_list = get_ip(headers)
    thread_list = []
    for i in ip_list:
        t = Crawl(i)
        t.start()
        thread_list.append(t)
        t.is_alive
    for t in thread_list:
        t.join()
        
    for s in thread_list:
        if s.run != None:
            print(s.run())
            break
