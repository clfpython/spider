# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from datetime import datetime
import time
import json
class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = time.time()
        item["spider"] = spider.name
        # with open("chaoxing.txt",'a',encoding='utf-8') as f:
        #     json.dump(item,f,ensure_ascii=False,indent=4)
        return item
