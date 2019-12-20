# -*- coding: utf-8 -*-
import scrapy
import json

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ["careers.tencent.com"]
    start_urls = ["https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576121680181&pageIndex=1&pageSize=10&language=zh-cn&area=cn"]


    # start_url 不会被域名限制，永远都会在第一次执行的时候，发送请求，获取响应并将响应传递给parse函数。
    def parse(self, response):
        # print(response.request.headers)
        # print(response.headers)
        # print(response.url)
        current_page_num = response.url.split("&")[1].split('=')[1]
        print(current_page_num)
        # response 有 body == content   ， text == text
        # print(response.text)
        # print("*"*100)
        # print(response.body.decode("utf-8"))
        json_str = response.body.decode()
        data = json.loads(json_str)
        data_list = data['Data']['Posts']
        for data in data_list:
            post_id = data["PostId"]  # 1204946654294183936
            post_url = data["PostURL"]  # "http://careers.tencent.com/jobdesc.html?postId=0"
            item = {}
            item["new_url"] = post_url.replace("0", post_id)
            item["name"] = data["RecruitPostName"]
            item["content"] = data["Responsibility"].replace("\n",'')
            print('-------------------------')
            print(item)
            print('-------------------------')
            url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1576131088321&postId={}&language=zh-cn".format(post_id)
            yield scrapy.Request(url,callback=self.parse_detail,meta=item)


        print('*'*100)
        print('*'*100)
        print('*'*100)

        # # 当前页码爬取完毕之后，继续爬下一页（判断是否有下一页）
        # if len(data_list) < 10:
        #     pass
        # else:
        #     print(current_page_num)
        #     next_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576118224354&pageIndex={}&pageSize=10&language=zh-cn&area=cn".format(int(current_page_num)+1)
        #     print(next_url)
        #     yield scrapy.Request(next_url,callback=self.parse)


    def parse_detail(self,response):
        item = response.meta
        response_data = response.body.decode()
        data = json.loads(response_data)

        item['duty'] = data['Data']["Responsibility"]
        item['requirement'] = data['Data']["Requirement"]
        print('/////////////////////////')
        print(item)
        print('/////////////////////////')

        yield item

        # with open('tencentdata_3.txt','a',encoding='utf-8')as f:
        #     json.dump(item,f,ensure_ascii=False,indent=4)



