import scrapy
from urllib.parse import urljoin  # python3中的urljoin

class TupianSpider(scrapy.Spider):
    name = "tupian"
    allowed_domains = ["desk.zol.com.cn"]
    start_urls = ["https://desk.zol.com.cn/dongman/"]

    def parse(self, response):
        print(response.url)
        li_list =response.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href').extract()
        for li in li_list:
            # 屏蔽掉不需要的图片
            if li.endswith('.exe') or li.endswith('.zip'):
                continue
            # 构建完整的url地址
            url = urljoin(response.url, li)
            # print(url)
            # 发送请求
            yield scrapy.Request(url=url, callback=self.parse_detail)
            # break


    def parse_detail(self, response):
        # print(response.url)
        # 处理详情页
        # 获取图片的url地址
        img_src = response.xpath('//img[@id="bigImg"]/@src').extract_first()
        # print('imgsrc==',img_src)
        #返回item
        yield {
            'img_src':img_src
        }
      
