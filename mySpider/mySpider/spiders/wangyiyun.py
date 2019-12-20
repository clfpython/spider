# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)

class WangyiyunSpider(scrapy.Spider):
    name = 'wangyiyun'      # 爬虫的名字,启动时候使用
    allowed_domains = ['music.163.com']     # 可爬取的范围
    start_urls = ['https://music.163.com/playlist?id=402385722']  # 爬虫的起始url

    def parse(self, response):
        logging.error("this is my parse-----error")
        logging.debug("this is my parse-----debug")
        logger.critical('this is critical')
        print('*'*100)
        print(response)
        print('*'*100)
        music_list = response.xpath('//ul[@class="f-hide"]/li/a/text()').extract()
        music_list = response.xpath('//ul[@class="f-hide"]/li/a/text()').extract_first()
        # print(music_list)  # extract 提取data中的数据
        item = {}
        item['歌曲列表'] = music_list
        # print(item)
        item = {"hello world":123}
        # for m in response.xpath('//ul[@class="f-hide"]/li/a/text()'):
        #     print(m.extract())
        # return item
        yield item


