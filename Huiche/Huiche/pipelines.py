# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
# from scrapy.pipelines.images import ImagesPipeline
import re
from scrapy.exceptions import DropItem
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline


class HuichePipeline(ImagesPipeline):
    def file_item(self,request,response=None,info=None):
        url = response.url
        file_name = url.split('/')[-1]
    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('Images Downloaded Field')
        return  item
    def get_media_requests(self, item, info):
        # for img_url in item['down_img']:
        yield Request(item['down_img'])
    # def item_completed(self,results,item,info?):
    #     return item