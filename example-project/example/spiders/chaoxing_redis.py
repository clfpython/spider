from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
import re
from copy import deepcopy
from scrapy_redis.spiders import RedisSpider
class ChaoxingRedisSpider(RedisSpider):
    """Follow categories and extract links."""
    name = 'chaoxing_redis'
    allowed_domains = ['book.chaoxing.com']
    # start_urls = ['http://book.chaoxing.com/']
    redis_key = 'chaoxing_start_url'
    def parse(self, response):
        # li_list = response.xpath("//ul[@class='All_list']/li")
        li_list = response.xpath("//ul[@class='All_list']/li")[0:2]

        for li in li_list:
            item = {}
            item["first_label"] = li.xpath('./a/text()').extract_first()
            a_list = li.xpath('./div/a')
            for a in a_list:
                item["second_label"] = a.xpath("text()").extract_first()
                a_href = "http://book.chaoxing.com" + a.xpath("@href").extract_first()
                item["a_href"] = a_href
                yield scrapy.Request(url=a_href,callback=self.parse_book_list,meta=item)

    def parse_book_list(self, response):
        item = response.meta
        book_list = response.xpath("//ul[@class='list']/li")
        for book in book_list:
            item["book_title"] = book.xpath("./div[2]/div[1]/p/a/text()").extract_first()
            a_href = "http://book.chaoxing.com" + book.xpath("./div[2]/div[1]/p/a/@href").extract_first()
            item["book_author"] = book.xpath("./div[2]/p[1]/span/text()").extract_first()
            yield scrapy.Request(url=a_href,callback=self.parse_book_detail,meta=item)
        # print(response.url)
        # 翻页：

        ret = re.search(r'/nPage_(\d+)/size',response.url)
        print(ret)
        current_page = ret.group(1)
        print(current_page)

        # 判断当前页码的数量
        # http://book.chaoxing.com/search/keyword_/fenleiID_0106/field_01/sortName_/nPage_2/size_10.html
        if len(book_list)<10:
            pass
        else:
            url_path_list = response.url.split("/")
            # nPage_2
            url_path_list[-2] = "nPage_" + str(int(current_page) +1)
            url = "/".join(url_path_list)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_book_list, meta=item)


        # end_page_href = response.xpath("//div[@id='pager']/a[last()]/@href").extract_first()
        # print('                 ',end_page_href)
        # if end_page_href is None:
        #     pass
        # else:
        #     ret = re.search(r'/nPage_(\d+)/size', end_page_href)
        #     end_page = ret.group(1)
        #     print(end_page_href)
        #     print(end_page)
        #     if current_page != end_page:
        #         url = "http://book.chaoxing.com/search/keyword_/fenleiID_1820/field_01/sortName_/nPage_{}/size_10.html".format(int(current_page)+1)
        #         yield scrapy.Request(url=url,callback=self.parse_book_list,meta=item)


    def parse_book_detail(self,response):
        item = response.meta
        item["publisher"] = response.xpath("//ul[@class='text01']/li[3]/text()").extract_first()
        item["type"] = response.xpath("//ul[@class='text01']/li[last()]/a/text()").extract_first()
        yield item

