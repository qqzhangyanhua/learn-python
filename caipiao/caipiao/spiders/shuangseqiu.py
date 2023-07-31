import scrapy


class ShuangseqiuSpider(scrapy.Spider):
    name = "shuangseqiu"
    allowed_domains = ["sina.com.cn"]
    start_urls = [
        "https://view.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs&type=50&dpc=1"]

    def parse(self, response):
        tbody = response.xpath('//*[@id="cpdata"]/tr')
        for tr in tbody:
            qi = tr.xpath('./td[1]/text()').extract_first()
            red = tr.xpath(
                './td[@class="chartball01" or @class="chartball20"]/text()').extract()
            if not red:
                continue
            blue = tr.xpath(
                './td[@class="chartball02"]/text()').extract_first()
            yield {
                'qi': qi,
                'red': red,
                'blue': blue
            }
