# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TulingPipeline(object):

    def open_spider(self,spider):
        print('this is open_spider')
        self.f = open('tuling.txt','w',encoding='utf-8')


    def close_spider(self,spider):
        print('this is close_spider')
        self.f.close()

    def process_item(self, item, spider):
        if spider.name == 'tulingbook':
            # self.f.write(json.dumps(item)+"\n")
            json.dump(item,self.f,ensure_ascii=False,indent=4)
            # with open('tencentdata_4.txt','a',encoding='utf-8')as f:
            #     json.dump(item,f,ensure_ascii=False,indent=4)
