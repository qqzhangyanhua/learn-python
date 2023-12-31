import scrapy
from scrapy import Request

class CheSpider(scrapy.Spider):
    name = "che"
    allowed_domains = ["che168.com"]
    start_urls = ["http://www.che168.com/shanghai/list/"]

    def parse(self, response):
        hrefs = response.xpath('//ul[@class="viewlist_ul"]/li/a/@href').extract()
        for href in hrefs:
            child_url =response.urljoin(href)
            yield Request(url=child_url, callback=self.parse_detail)

        # 获取下一页的链接
        # 1. 获取下一页的链接
        page = response.xpath('//div[@id="listpagination"]/a/@href').extract()
        for p in page:
            if p != 'javascript:;':
                next_url = response.urljoin(p)
                yield Request(url=next_url, callback=self.parse)
        # 2. 发送请求
        # 3. 解析数据
        # 4. 保存数据

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
