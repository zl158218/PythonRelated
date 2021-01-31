# coding:utf-8
# 待添加异常处理
import re,requests,os,time
from urllib.parse import urlencode
from lxml import etree
import json
import jsonpath

def get_index(offset,keyword):
    '''获取json，提取image的url，提取title'''
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from':'gallery'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'content-type': 'text/html; charset=utf-8',
        'Cookie':'tt_webid=6618053030305826317'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        paser = requests.get(url,headers=headers)
        if paser.status_code == 200:
            # print(paser.json())
            return paser.json()
    except requests.ConnectionError:
        return None

def img_url(json):
    # 生成图集的url
    # print(json)  
    if json.get('data'):
        for item in json.get('data'):
            titles = item.get('title')
            # print(titles)  # 图集title
            imgs_url = item.get('article_url')
            # print(imgs_url) #图集 url
            yield {
                    'image':imgs_url,
                    'title':titles
                }

def parse_img(img_url):
    #请求获取图集url，并get图片
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'content-type': 'text/html; charset=utf-8',
        'Cookie':'tt_webid=6618053030305826317'
    }
    for img in img_url:
        time.sleep(0.5)
        if len(img['image']) < 50:
            # print(img['image'])     # 打印 图片集 的url 结果一：‘https://www.toutiao.com/a6632552154257162766/’
            html = requests.get(url=img['image'],headers=headers).text
            titles = re.search('.*?title\:\s\'(.*?)\'\,',html,re.S).group(1)   #图片名字
            # print(titles)
            pattern = re.compile(r'.*?\"url_list\"\:\[\{(.*?)\},.*?\,',re.S)   # 定义一个Pattern
            urls = re.findall(pattern,html.replace("\\","").replace("\]","").strip())   # 匹配图片的url
            path = '/home/aim/test/img/'       # 图片路径
            if not os.path.exists(path):
                os.makedirs(path)                

            for url in urls:
                time.sleep(0.5)
                imgs = requests.get(url=url[7:-1],headers=headers)
                filename = url[-14:-1] + '.jpg'    # 图片名字
                print()

                if not os.path.exists(filename):
                    os.system(r"touch {}".format(filename))  #调用系统命令行来创建文件
                # for i in imgs:
                    with open(path+filename,"wb") as f:
                        for binary in imgs:
                        
                            f.write(binary)
                        print("Images Dowloads successful")
                        print(url[7:-1])
                
def main():
    for i in range(0,120,20):
        offset = i
        json = get_index(offset,'街拍')
        imgs = img_url(json)
        parse_img(imgs)

import sys

def error_line():
    s = sys.exc_info()
    return "errLine {} ".format( s[2].tb_lineno)

print(sys._getframe().f_lineno)
try:
    print(str(2.9))
    t = 1
    t2 = "1"
    t3 = t + t2
    
except Exception as e:
    print(error_line())
    print(sys._getframe().f_lineno)

if __name__ == '__main__':
    main()