import scrapy


class CheSpider(scrapy.Spider):
    name = "che"
    allowed_domains = ["168.com"]
    start_urls = ["https://168.com"]

    def parse(self, response):
        pass
