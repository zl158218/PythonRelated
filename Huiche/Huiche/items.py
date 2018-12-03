# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuicheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图集名字
    titles = scrapy.Field()

    # 图集的url
    url_list = scrapy.Field()

    # 图集里面所有图片的url
    imgs = scrapy.Field()

    # 图片下载地址
    down_img = scrapy.Field()

