# -*- coding:utf-8 -*-
"""
@描述： 单个爬虫/接口请求，作为模板用, 
@时间： 2020-10-14
@作者： 十叁

"""

import warnings
import requests
from lxml import etree
from loguru import logger

warnings.filterwarnings("ignore")

class Temp:

    def __init__(self):
            
        self.headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.session = requests.Session()

    def run(self):
        self.details()

    def details(self, retry: int = 0):
        '''
        详细信息
        :return:
        '''
        if retry > 5:
            return []
        
        try:
            url = "https://www.baidu.com"
            response = self.session.get(url=url, headers=self.headers, timeout=15, verify=False)
            logger.info(response.url)
            
            # 解码 | 防止页面编码错误
            response.encoding = response.apparent_encoding
            logger.info(response.text)
            logger.info(len(response.text))
            
            html = etree.HTML(response.text)
            for detail in html.xpath('//div//h1'):
                # 转为 HTML 文本
                print(etree.tounicode(detail))
            
        except Exception as exc:
            logger.info(f"抓取失败 {exc}")

def main():
    logger.info(f'开始抓取...')
    Temp().run()
    logger.info(f'抓取完成...')
   

if __name__ == '__main__':
    main()