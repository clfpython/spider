# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import MyspiderItem
class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['www.jingdong.com']
    start_urls = ['http://www.jingdong.com/']

    def parse(self, response):
        item = MyspiderItem()
        # item = {}
        item["name"] = 'zzh'
        item['age'] = 18
        item['sex'] = 1
        item['height'] = 178
        yield item