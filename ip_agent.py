# coding:utf-8
'''
ip 代理
本次用的 https 类型， http 代理自行调整。
HTTPS只是在http与tcp之间加了一个ssl层
'''
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
                    proxies = {'https': 'http://' + ip[0] + ":" + ip[1]}
                    # print(proxies)
                    # url = 'https://www.douban.com/'
                    url = 'https://www.baidu.com/'
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
    # print(ip)
	
# proxies = {'http': 'http://localhost:8888'}    # proxies
# r = requests.get("http://ip.chinaz.com/", proxies=proxies, timeout=3)   设置proxies
