# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        di = {}
        di['name'] = 'zhangsan'
        yield di
