# -*- coding: utf-8 -*-
# 回车桌面美女标签
import scrapy
import re
from Huiche.items import HuicheItem
from scrapy.http import Request
from urllib import parse

class DeskSpider(scrapy.Spider):
    name = 'Desk'
    allowed_domains = ['mm.enterdesk.com']
    start_urls = ['https://mm.enterdesk.com/']
    for i in range(1,5):
        url = 'https://mm.enterdesk.com/' + str(i) + '.html'
        start_urls.append(url)

    def parse(self, response):
        item = HuicheItem()

        # 获取title
        item['titles'] =  response.xpath('//*[@class="egeli_pic_dl"]//dt//a//text()').extract()
        # 获取标签url
        url_list = response.xpath('//*[@class="egeli_pic_dl"]//dt//a/@href').extract()
        for urls in url_list:
            item['url_list'] = urls
            yield scrapy.Request(url=item['url_list'],callback=self.parse_url,meta={'item':item['url_list']})
            #print(urls)  打印获取的 url

    def parse_url(self,response):
        item = HuicheItem()

        item_list = response.meta['item']     #接收一下 item

        # print(response.text)   #打印获取所有url的html页面

        #获取二级页面 images 的 url
        image_list_url = response.xpath('//*[@class="swiper-wrapper"]/div/a/@href').extract()
        # print(response.url,'第一级的url'ur)
        for imgs in image_list_url:
            # item['imgs'] = imgs
            # print(item['imgs'])
            # print(imgs)
            # 二级标签所有的images 预览图的url
            urls = parse.urljoin(response.url,imgs)
            yield scrapy.Request(url=urls,meta={'img_url':urls},callback=self.get_imgs_url)

    #获取images 的 url 下载 地址
    def get_imgs_url(self,response):
        item = HuicheItem()
        imgs = response.meta['img_url']
        # print(imgs)

        get_imgs_urls = response.xpath('//*//div[@id="images_show_zoom"]//@href').extract()   # 获取 查看图片的 href

        # 拼接 url
        for  url in get_imgs_urls:
            img = {'key':'https:'+url}
            # img = 'https:' + url

            yield scrapy.Request(url=img['key'], callback=self.down_url, meta={'images':img['key']},dont_filter=True)

    def down_url(self,response):
        # print("三级url，开始")
        item = HuicheItem()
        dowload_images_urls = response.meta['images']
        # print(dowload_images)   # 测试是否打印url
        # print(response.text)    # 测试是都正常输出HTML信息
        down_imgs = response.xpath('//*//a[@id="images_show_downa"]//@href').extract()[0]
        item['down_img'] = response.xpath('//*//a[@id="images_show_downa"]//@href').extract()[0]
        # print(item['down_img'])
        yield item



        # print(down_imgs[0])


        # response.url()



    # print(img)
    # print(type(img))
    # print(item['down_img'])

    # imgs_url = ('https:' + url)   #原图的html 页面

    #for dow_img in downloads_url:

    # item['down_img'] =
    # print(imgs_url)
    # yield scrapy.Request(url=item['down_img'],meta={'down_imgs':imgs_url},callback=self.down_img)

    # def down_img(self,response):
    #
    #
    #
    #     img = response.meta['down_imgs']
    #     print(img)
    #     get_images = response.meta['']



    #
    # def down_img(self,response):
    #     item = HuicheItem()
    #     down_imgs = response.meta[]

        # down_imgs = response.meta['down_img']
        # print(down_imgs)




    # yield scrapy.Request(url=imgs_url,meta={'get_imgs':str(imgs_url)},callback=self.down_imgs)
    #
    # def down_imgs(self,response):
    #     item = HuicheItem()
    #     get_imgs = response.meta['get_imgs']
    #     print(get_imgs)



    # imgs = parse.urljoin(response.url,img)
    # print(imgs)
    # print(response.url)
    # print(sta)
    # ['//www.enterdesk.com/download/35463-211040/']
    # print(imgs)



    #//*//div[@id="images_show_zoom"]//@href

    # item3 = response.meta['item2']

    # yield scrapy.Request()

    #     yield Request(url=item['pageURL'], meta={'item2': item}, callback=self.parse_three)
    #
    #     yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
    #                   callback=self.parse_content)
    # print(urls)

    # Request(url=item_list,callback=self.parse_image)
    #
    # def parse_image(self,response):
    #     img = response.xpath('/html/body/div[10]/div[1]/div[4]/div/div[1]/div[1]/a/img@src(0)')
    #     print(img)




    # item['url_list'] = response.xpath('//*[@class="egeli_pic_dl"]//dt//a/@href').extract()
    # item['url_list'] =
    # return url_list
    # def parse_page1(self, response):
    #     item = MyItem()
    #     item['main_url'] = response.url
    #     request = scrapy.Request("http://www.example.com/some_page.html",
    #                              callback=self.parse_page2)
    #     request.meta['item'] = item
    #     return request
    #
    # def parse_page2(self, response):
    #     item = response.meta['item']
    #     item['other_url'] = response.url
    #     return item