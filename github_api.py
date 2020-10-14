# -*- coding: UTF-8 -*-
"""
@描述： 小爬虫| 作为模板用
@时间： 2020-10-14
@作者： 十叁
@API限制： https://api.github.com/rate_limit

"""
import os
import time
import pygal
import warnings
import requests
from lxml import etree
from loguru import logger
from selenium import webdriver
from warnings import showwarning
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

warnings.filterwarnings("ignore")

class GitHubAPI:

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
        self.temp_html :dict = ''

    def run(self):
        self.search()
        # self.data_treat()
        self.bar_descriptions()
        self.open_svg()
        
        
    def search(self, retry: int = 0):
        '''
        查询
        :return:
        '''
        if retry > 5:
            return []
        
        try:
            url = "https://api.github.com/search/repositories?q=language:python&sort=start"
            response = self.session.get(url=url, headers=self.headers, timeout=15, verify=False)
            logger.info(response.url)
            
            # 解码 | 防止页面编码错误
            response.encoding = response.apparent_encoding
            # logger.info(response.json())
            logger.info(len(response.text))
            logger.info(f"Status Code: {response.status_code}")
            
            self.temp_html = response.json()
            
            # html = etree.HTML(response.text)
            # for detail in html.xpath('//div//h1'):
            #     # 转为 HTML 文本
            #     print(etree.tounicode(detail))
            
        except Exception as exc:
            logger.info(f"抓取失败 {exc}")

    def data_treat(self):
        total_count = self.temp_html.get('total_count')
        logger.info(f"Total_count: {total_count}")
        
        names, starts = [], []
        
        for repo_dict in self.temp_html.get('items'):
            names.append(repo_dict.get('name'))
            starts.append(repo_dict.get('stargazers_count'))
        
        my_style = LS('#333366', base_style=LCS)
        my_config = pygal.Config()
        my_config.x_label_rotation = 45
        # X 轴旋转度数
        
        my_config.show_legend = False
        # 隐藏图列
        
        my_config.title_font_size = 24
        my_config.label_font_size = 14
        my_config.major_label_font_size = 18
        my_config.truncate_label = 15
        my_config.show_y_guides = False
        my_config.width = 1000
        # 自定义宽度
        
        chart = pygal.Bar(my_config, style=my_style)
        chart.title = "Most-Starred Python Project on GitHub"
        chart.x_labels = names
        chart.add('Start: ', starts)                
        chart.render_to_file('python_repos.svg')

    def bar_descriptions(self):
        
        names, plot_dicts = [], []
        
        for repo_dict in self.temp_html.get('items'):
            names.append(repo_dict.get('name'))
            plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': repo_dict['description'],
                'xlink': repo_dict['html_url']
            }
            plot_dicts.append(plot_dict)
            
        
        my_style = LS('#333366', base_style=LCS)
        chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
        chart.title = "Python Projects"
        chart.x_labels = names
        chart.add('', plot_dicts)
        chart.render_to_file('python_repos.svg')                

    def open_svg(self):
        """
        打开 SVG 文件
        """
        self.chrome_ops = webdriver.ChromeOptions()
        self.chrome_ops.add_argument('--ignore-certificate-errors')
        self.chrome_ops.add_experimental_option("detach", True)
        # 设置屏幕大小
        self.chrome_ops.add_argument('--window-size=1980,1080')
        browser = webdriver.Chrome(options=self.chrome_ops)
        browser.get('file:///'+ os.path.abspath('python_repos.svg'))
        time.sleep(60)

def main():
    logger.info(f'开始抓取...')
    GitHubAPI().run()
    logger.info(f'抓取完成...')
   

if __name__ == '__main__':
    main()