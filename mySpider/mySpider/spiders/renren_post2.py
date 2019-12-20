# -*- coding: utf-8 -*-
import scrapy


class RenrenPost2Spider(scrapy.Spider):
    name = 'renren_post2'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response,
                                               formdata={"email":"18669319099", "password":"python123456"},
                                               callback=self.parse2
                                               )



    def parse2(self,response):
        with open("renren4.html","w",encoding="utf-8") as f:

            f.write(response.body.decode())
