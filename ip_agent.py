# coding:utf-8
import requests
import re
import random

def get_ip():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    for i in range(1, 10):
        page = random.randint(1, 10)  # 随机页数，自行调整
        url = 'https://www.xicidaili.com/nn/' + str(i)  # 国内高匿代理IP
        html = requests.get(url, headers=headers).text
        pattern = re.compile('<td>([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)</td>.*?<td>(\d*?)</td>.*?<td>([A-Z]*)</td>', re.S)
        ips = pattern.findall(html)
        for ip in ips:
            if str(ip[2]) == "HTTPS":
                try:
                    proxies = {'https': 'https://' + ip[0] + ":" + ip[1]}
                    url = 'https://www.163.com/'
                    douban = requests.get(url, headers=headers, proxies=proxies, timeout=1)
                    if douban.status_code == 200:
                        # print(proxies)
                        return proxies
                except:
                    continue
                else:
                    print('success')

if __name__ == "__main__":
    ip = get_ip()
    print(ip)
