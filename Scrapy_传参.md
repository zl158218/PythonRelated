# 方法1
#coding:utf-8
#导入模块
import scrapy
import re
from Huiche.items import HuicheItem

class DeskSpider(scrapy.Spider):
    name = 'Desk'
    allowed_domains = ['mm.enterdesk.com']
    start_urls = ['https://mm.enterdesk.com/']
    
    def parse(self, response):
        item = HuicheItem()
        #获取title
        item['titles'] =  response.xpath('//*[@class="egeli_pic_dl"]//dt//a//text()').extract()
        #获取所有标签url
        url_list = response.xpath('//*[@class="egeli_pic_dl"]//dt//a/@href').extract()
        #传参，用 callback=self.parse_url,meta={'item':item}
        for urls in url_list:
            item['url_list'] = urls            
            yield scrapy.Request(url=item['url_list'],callback=self.parse_url,meta={'item':item})

    def parse_url(self,response):
        item = response.meta['item']
        print(item)
   


# 方法2
     #def parse_page1(self, response):
     #    item = MyItem()
     #    item['main_url'] = response.url
     #    request = scrapy.Request("http://www.example.com/some_page.html",callback=self.parse_page2)                    
     #    request.meta['item'] = item
     #    return request
     #
     #def parse_page2(self, response):
     #    item = response.meta['item']
     #    item['other_url'] = response.url
     #    return item

- 都类似，能看懂哪个用哪个。
