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
