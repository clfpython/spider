# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TulingSpider(CrawlSpider):
    name = 'tuling'
    allowed_domains = ['www.ituring.com.cn']
    start_urls = ['https://www.ituring.com.cn/tag/11']



    rules = (
        Rule(LinkExtractor(allow=r'book/(\d+)'), callback='parse_item',),
        Rule(LinkExtractor(allow=r'tag/books/11\?page=(\d+)'),follow=True),

        # follow： 连接提取器提取出来的url地址对应的响应是否继续被rules来过滤提取。
    )

    def parse_item(self, response):
        print(response.url)
        print(response.request.url)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item


    # def parse_page(self,response):
    #     print(response.url)
    #     print(response.request.url)

