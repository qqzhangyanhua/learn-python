import scrapy


class YouxiSpider(scrapy.Spider):
    name = "youxi"
    allowed_domains = ["4399.com"]
    start_urls = ["https://4399.com"]

    def parse(self, response):
        pass
