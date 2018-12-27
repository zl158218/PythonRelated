# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from  urllib.parse import urlencode

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print(response.text)
        datas = response.xpath('//div[@class="quote"]')
        for data in datas:
            item = TutorialItem()
            item['text'] = data.xpath('./span[@class="text"]/text()').extract()[0]            # 名言
            item['author'] = data.xpath('.//small[@class="author"]/text()').extract()[0]      # 作者
            Tags = data.xpath('.//a[@class="tag"]/text()').extract()
            item['tags'] =  ",".join(Tags)                                                    # 标签
            yield item

        next = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next is not None:
            next_url = response.urljoin(next)
            yield scrapy.Request(url=next_url,callback=self.parse)


            # print(tags,'\n',text,'\n',author)




'''
import scrapy
from tutorial.items import TutorialItem
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        url = 'http://quotes.toscrape.com/tag/humor/'
        yield scrapy.Request(url)
    def parse(self, response):
        item = TutorialItem()
        for quote in response.css('div.quote'):
        item['body'] = quote.css('span.text::text').extract_first()
        item['author'] = quote.css('small.author::text').extract_first()
            yield item
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

'''