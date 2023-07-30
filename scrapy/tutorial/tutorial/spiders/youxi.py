import scrapy


class YouxiSpider(scrapy.Spider):
    name = "youxi"
    allowed_domains = ["4399.com"]
    start_urls = ["http://www.4399.com/flash/"]
    ret_list = []
    def parse(self, response):
        # print(response)
        li_list =response.xpath('//*[@id="skinbody"]/div[8]/ul/li')
        # print(li_list)
        for li in li_list:
            name =li.xpath('./a/b/text()').extract_first()
            fenlei =li.xpath('./em/a/text()').extract_first()
            create_time =li.xpath('./em/text()').extract_first()
            yield{
                'name':name,
                'fenlei':fenlei,
                'create_time':create_time
            }
    def save(self):
        pass
