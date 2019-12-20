# -*- coding: utf-8 -*-
import scrapy
import time
import re
from copy import deepcopy
class TulingbookSpider(scrapy.Spider):
    name = 'tulingbook'
    allowed_domains = ['ituring.com.cn']
    start_urls = ['https://www.ituring.com.cn/']

    def parse(self, response):
        cookies = "__utma=1.1778907961.1576217073.1576217073.1576217073.1; __utmc=1; __utmz=1.1576217073.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __RequestVerificationToken=5kOz0_Bzu720MGu-ZwqRfMPpPWROA-7EE_93G7kTa3dQcYcSsyIoGny6VI45TGqYIhmpnb9QyDbPrkW7kSYGPoaQSxLK8oipdRgyzlN0knM1; __utmt=1; __utmb=1.25.10.1576217073"
        self.cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split(';')}
        html_content = response.body.decode()
        a_list = response.xpath('//span[@class="tags"]/a')
        print(a_list)
        for a in a_list:
            # print(a.xpath("./@href").extract()[0])
            item = {}
            item['tags'] = a.xpath("./text()").extract_first()
            print(item["tags"])

            href = a.xpath("./@href").extract_first()
            list_url = "https://www.ituring.com.cn" + href
            ret = re.search('/tag/(\d+)', href)
            item["tag_id"] = ret.group(1)
            time.sleep(1)
            yield scrapy.Request(url=list_url, callback=self.parse_list, cookies=self.cookies, meta=item,
                                 dont_filter=True)

        # a = a_list[0]
        # # print(a.xpath("./@href").extract()[0])
        # item = {}
        # item['tags'] = a.xpath("./text()").extract_first()
        # print(item["tags"])
        #
        # href = a.xpath("./@href").extract_first()
        # list_url = "https://www.ituring.com.cn" + href
        # ret = re.search('/tag/(\d+)',href)
        # item["tag_id"] = ret.group(1)
        # time.sleep(1)
        # yield scrapy.Request(url=list_url, callback=self.parse_list,cookies=self.cookies, meta=item, dont_filter=True)



    def parse_list(self,response):
        item = response.meta
        # item2 = deepcopy(item)
        # item = {}
        a_list = response.xpath("//ul[@class='block-items']/li/div[2]/h4/a")
        print(a_list)
        for a in a_list:
            item["book_title"] = a.xpath("./text()").extract_first()
            href = a.xpath("./@href").extract_first()
            list_url = "https://www.ituring.com.cn" + href
            print(list_url)
            time.sleep(1)
            yield scrapy.Request(url=list_url,callback=self.parse_detail,cookies=self.cookies,meta=item)

        # 翻页：
        if len(a_list) == 20 :
            # 说明是最后一页，不需要翻页
            current_page_num = response.xpath("//div[@class='PagedList-pager']/ul//li[@class='PagedList-disabled PagedList-currentPage PagedList-skipToPage']/a/text()").extract_first()
            print('*'*100)
            print(current_page_num)
            print('*'*100)
            url ="https://www.ituring.com.cn/tag/books/{}?page={}&X-Requested-With=XMLHttpRequest&_=1576224163555".format(item["tag_id"],current_page_num)
            yield scrapy.Request(url=url,callback=self.parse_list,meta=item,cookies=self.cookies)

    def parse_detail(self,response):
        item = response.meta
        # item = {}
        item["read_no"] = response.xpath('//*[@id="book-fav-vote"]/div/span[1]/text()').extract_first()
        print(item)
        yield item

