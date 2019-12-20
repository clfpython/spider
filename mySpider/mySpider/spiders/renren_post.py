# -*- coding: utf-8 -*-
import scrapy


class RenrenPostSpider(scrapy.Spider):
    name = 'renren_post'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):
        yield scrapy.FormRequest(url="http://www.renren.com/PLogin.do",
                                 formdata={"email":"18669319099","password":"python123456"},
                                 callback=self.parse2)
    def parse2(self,response):
        with open("renren3.html","w",encoding="utf-8") as f:

            f.write(response.body.decode())
