# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道的作用：清洗数据，整理数据格式，保存在本地、数据库
class MyPipelinePipeline(object):
    def process_item(self, item, spider):
        print('1111111111111111111')
        item["age"] = 18
        print(item)
        # return item
        return None
class MyPipelinePipeline2(object):
    def process_item(self, item, spider):
        print('222222222222222')
        print(item)
        # item["SEX"] = 'male'
        # print(item)
        return item


class MyPipelinePipeline3(object):
    def process_item(self, item, spider):
        print('333333333333')
        # item["height"] = 180
        print(item)
        return item

