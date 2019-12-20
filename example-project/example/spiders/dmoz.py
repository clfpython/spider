from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import scrapy
class DmozSpider(scrapy.Spider):
    """Follow categories and extract links."""
    name = 'dmoz'

    allowed_domains = ['book.chaoxing.com']
    start_urls = ['http://book.chaoxing.com/']


    def parse(self, response):
        # li_list = response.xpath("//ul[@class='All_list']/li")
        li_list = response.xpath("//ul[@class='All_list']/li")[1]
        li2 = []
        li2.append(li_list)
        for li in li2:
            item = {}
            item["first_label"] = li.xpath('./a/text()').extract_first()
            a_list = li.xpath('./div/a')
            for a in a_list:
                item["second_label"] = a.xpath("text()").extract_first()
                a_href = "http://book.chaoxing.com" + a.xpath("@href").extract_first()
                item["a_href"] = a_href
                yield scrapy.Request(url=a_href, callback=self.parse_book_list, meta=item)

    def parse_book_list(self,response):

        yield response.meta