import scrapy
from scrapy import Request
# 连接提取器
from scrapy.linkextractors import LinkExtractor
class CheSpider(scrapy.Spider):
    name = "che"
    allowed_domains = ["che168.com"]
    start_urls = ["http://www.che168.com/shanghai/list/"]

    def parse(self, response):
      # 创建一个提取器
      lktor = LinkExtractor(restrict_xpaths='//ul[@class="viewlist_ul"]/li/a')
      # 提取所有的链接
      links = lktor.extract_links(response)
        # 遍历所有的链接
      for link in links:
          yield Request(link.url, callback=self.parse_detail)
   


    def parse_detail(self, response):
        title = response.xpath('//h3[@class="car-brand-name"]/text()').extract_first()
        price = response.xpath('//span[@class="price"]/text()').extract_first()
        # 去掉空格
        if title:
            title = title.strip()
        if price:
            price = price.strip()
        print('=====================')
        print(title,'==============',price ,response.url)
        yield {
            'title': title,
            'price': price,
            'url': response.url
        }
