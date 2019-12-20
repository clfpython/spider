# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']

    start_urls = ['http://www.renren.com/973016491/profile']

    cookies = "anonymid=k3xtgnw7-hlci4r; _r01_=1; depovince=SD; jebecookies=6f39faea-f275-428b-b45a-32f7323d35c9|||||; JSESSIONID=abcaOEA36K6tJdTqlUm8w; ick_login=82db3417-60a8-4de5-8d80-70a8dead7162; _de=E0E61E21D5EC0F38439512C7FDDF72C8; p=0a6ee96a7321659509b4be74fd0e56541; first_login_flag=1; ln_uact=18669319099; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=d5a65b29ed04326f7266c43a3d5a9c831; societyguester=d5a65b29ed04326f7266c43a3d5a9c831; id=973016491; xnsid=f34658ec; ver=7.0; loginfrom=null; jebe_key=d03a7801-f25b-4742-9803-015d8942fa08%7Cd602d7aea178b0018804f4f7bc8b6cb7%7C1576466494103%7C1%7C1576466501572; jebe_key=d03a7801-f25b-4742-9803-015d8942fa08%7Cd602d7aea178b0018804f4f7bc8b6cb7%7C1576466494103%7C1%7C1576466501574; wp_fold=0"
    cookies = {di.split("=")[0]: di.split("=")[1] for di in cookies.split(";")}

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, cookies=self.cookies
                             # meta={'proxy':"114.104.183.93:44958"
                             #       }
                             )

    def parse(self, response):
        # print(response.body.decode())
        with open("renren.html",'w',encoding='utf-8') as f:
            f.write(response.body.decode())
        yield scrapy.Request(url="http://www.renren.com/973016491/newsfeed/photo",callback=self.parse2)


    def parse2(self,response):
        with open("renren2.html", 'w', encoding='utf-8') as f:
            f.write(response.body.decode())

