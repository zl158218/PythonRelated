# 这是 scrapy 里面的spider
# -*- coding: utf-8 -*-

import scrapy
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['python.jobbole.com']
    start_urls = ['http://python.jobbole.com/all-posts/']
 
    def parse(self, response):
        # 构造请求 全部文章的 url
        
        '''
        css 方法
        post_urls=response.css("div#archive div.floated-thumb div.post-meta p a.archive-title::attr(href)").extract()
        print(post_urls)   
        for post in post_urls:
          yield scrapy.Request(post,callback=self.parse_detail)
        '''
        
        #xpath 方法  div里面的class="post-meta" 下一级  a标签 [@target="_blank"] 提取 href 属性
        post_urls=response.xpath('//div[@class="post-meta"]//a[@target="_blank"]//@href').extract()
        #print(post_urls)
        for post in post_urls:
            #传参给 parse_detail 函数
            yield scrapy.Request(post,callback=self.parse_detail)

    def parse_detail(self,response):
        # 打印请求 post 的 html
        print(response.text) 
