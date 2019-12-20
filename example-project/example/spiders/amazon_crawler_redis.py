from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class Amazon(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'amazon'
    redis_key = 'amazon_start_url'
    allowed_domains = ['www.amazon.cn']
    # https://www.amazon.cn/gp/book/all_category

    rules = (
        # follow all links
        # 分类url
        # Rule(LinkExtractor(restrict_xpaths=("//div[@id='content']//div[@class='a-row a-size-base']/div[2]//a")), follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='content']//div[@class='a-row a-size-base']/div[2]//a[@title='作品集']")), follow=True),
        # 详情页url
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//div[@class='a-row a-spacing-small']//a","//div[@class='s-result-list s-search-results sg-row']//a[@class='a-link-normal a-text-normal']")),callback="parse_detail", follow=False),
        # 翻页url
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']",'//div[@class="a-section s-border-bottom"]//a')), follow=True),
    )


    def parse_detail(self, response):
        item = {}
        item["first_label"] = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']/li[3]//a/text()").extract_first()
        item["second_label"] = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']/li[5]//a/text()").extract_first()
        item["title"] = response.xpath('//div[@id="booksTitle"]/div[1]/h1/span/text()').extract_first()
        item["author"] = response.xpath('//div[@id="booksTitle"]/div[2]/span[1]/a/text()').extract_first()
        item["price"] = response.xpath("//span[@class='a-size-base a-color-price a-color-price']/text()  | //span[@class='a-color-price']/text()").extract_first()
        yield item

# Git