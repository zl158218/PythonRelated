# coding:utf-8
import chardet
import requests
import re

def jd(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=' + str(page) +'&s=57&click=0'
    res = requests.get(url,headers=headers)
    res.encoding =chardet.detect(res.content)['encoding']

    price_re = '<strong class=".*?" data-done="\d"><em>￥</em><i>(.*?)</i></strong>'  # 匹配商品价格
    price_list =  re.findall(price_re,res.text,re.S)
    # print(price_list)
    
    store_re = '<a target="_blank" class="curr-shop" onclick=".*?" href="(.*?)" title=".*?">(.*?)</a>'   # 正则匹配店铺名字,及链接
    store_list = re.findall(store_re,res.text,re.S)
    # for i in range(len(store_list)):
    #     print('https:' + str(store_list[i][0]) + ", " + str(store_list[i][1]))   

    introduction_re = '<div class="p-name p-name-type-2">.*?<em>(.*?)</em>.*?</div>'   # 正则匹配简介
    introduction_list = re.findall(introduction_re,res.text,re.S)
    try:
        for i in range(len(price_list)):
            titles = re.sub('<.*?>','',introduction_list[i])
            print(titles)
            print("店铺名字: " + str(store_list[i][1]))
            print("店铺链接: " + 'https:' + str(store_list[i][0]) + ", ")
            print()
    except:
        return None

if __name__ == "__main__":
    for page in range(0,20,3):
        jd(page)
