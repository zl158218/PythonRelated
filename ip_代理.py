# coding:utf-8
import requests
import re
import random
import threading

def get_ip(headers):
    ip_list = []
    for page in range(2,10,int(random.choice(range(1,4)))):
        url = 'https://www.xicidaili.com/nn/' + str(page)  # 国内高匿代理IP
        proxies = {'https':'https://'+ '121.61.3.58:9999'}
        html = requests.get(url, headers=headers,proxies=proxies).text
        pattern = re.compile('<td>([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)</td>.*?<td>(\d*?)</td>.*?<td>([A-Z]*)</td>', re.S)
        ips = pattern.findall(html)
        ip_list = ip_list + ips
    return ip_list

def validation(headers,ip):
    for i in ip:
        if str(i[2]) == "HTTPS":
            proxies = {'https': 'https://' + i[0]+ ":" + i[1]}
            try:
                proxies = {'https': 'https://' + i[0]+ ":" + i[1]}
                url = 'https://www.163.com/'
                html = requests.get(url, headers=headers, proxies=proxies, timeout=1)
                if html.status_code == 200:
                        return proxies
                        break
            except:
                continue

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Connection': 'keep-alive'
    }
    ips = get_ip(headers)
    proxiex_ip = validation(headers,ips)
    # print(proxiex_ip)

if __name__ == "__main__":
    main()
