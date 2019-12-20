# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/%E6%B8%AF%E5%8F%B0']


    cookies = 'll="118221"; bid=BTOq7lJdzJo; __utmc=30149280; dbcl2="208092506:ff+CGKvgLxw"; ck=b8qs; gr_user_id=c41e751e-5d34-443c-8f59-3c61b5a22941; gr_cs1_f31d85e2-7400-4a3f-b17b-32f8c2a9b32d=user_id%3A1; _pk_ses.100001.3ac3=*; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1576490710%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fbook.douban.com%252F%22%5D; __utma=30149280.1021357975.1576468464.1576468464.1576490710.2; __utmz=30149280.1576490710.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=81379588.237068390.1576490710.1576490710.1576490710.1; __utmc=81379588; __utmz=81379588.1576490710.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __yadk_uid=R8AVVdGQXvmrdPqbPIoeXo1u9p3MfzVC; _vwo_uuid_v2=D2D9F7D13A68B39DBBAB81A7713E96A90|f817bd73a5da95f30b21d81566e03027; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20809; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=3889bf15-40a5-417c-9a6b-eab3bd2760c0; gr_cs1_3889bf15-40a5-417c-9a6b-eab3bd2760c0=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_3889bf15-40a5-417c-9a6b-eab3bd2760c0=true; __utmt_douban=1; __utmt=1; _pk_id.100001.3ac3=618f9e0a8685b681.1576490710.1.1576492955.1576490710.; __utmb=30149280.48.10.1576490710; __utmb=81379588.34.10.1576490710'
    cookies = {di.split("=")[0]:di.split("=")[1] for di in cookies.split(";")}

    def start_requests(self):
        yield scrapy.Request(url= self.start_urls[0],callback=self.parse,cookies=self.cookies
                             # meta={'proxy':"114.104.183.93:44958"
                             #       }
        )



    # ip 多次访问。用户代理。proxies
    rules = (
        # Rule(LinkExtractor(allow=r'tag/(\w+)$'), follow=True),
        Rule(LinkExtractor(allow=r'/tag/(\w+)?start=[(20)(40)(60)(80)]&type=(\w+)$'), follow=True),
        Rule(LinkExtractor(allow=r'/subject/(\d+)/$'), callback="parse_detail", follow=False),
    )


    # def parse_item(self, response):
    #     item = {}
    #     print(response.url)
    #     #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
    #     #item['name'] = response.xpath('//div[@id="name"]').get()
    #     #item['description'] = response.xpath('//div[@id="description"]').get()
    #     return item
    def parse_detail(self, response):
        item = {}

        item["author"] = response.xpath("//div[@id='info']/span[1]/a/text()").extract_first()
        item["publisher"] = response.xpath("//div[@id='info']/span[2]/following::text()[1]").extract_first()
        item["price"] = response.xpath('//div[@id="info"]/span[2]/following::text()[14]').extract_first()

        yield item

