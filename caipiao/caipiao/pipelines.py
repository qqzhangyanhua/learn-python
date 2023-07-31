# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
import scrapy

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CaipiaoPipeline:
    def open_spider(self, spider):
        print('爬虫开始了')
        self.f = open('shuangseqiu.csv', mode='w', encoding='utf-8')

    def close_spider(self, spider):
        print('爬虫结束了')
        self.f.close()

    def process_item(self, item, spider):
        self.f.write(f'{item["qi"]},{item["red"]},{item["blue"]}\n')
        return item


class CaipiaoPipeline_sql:
    def open_spider(self, spider):
        print('建立连接')
        self.conn = pymysql.connect(
            user='root',
            password='admin123',
            host='localhost',
            database='crawl',
        )
        self.f = open('sql.csv', mode='w', encoding='utf-8')

    def close_spider(self, spider):
        print('爬虫结束了sql')
        self.conn.close()

    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = 'insert into your_table_name(qi,red,blue) values(%s,%s,%s)'
            cursor.execute(
                sql, (item['qi'], '_'.join(item['red']), item['blue']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        print('写入成功')
        return item

# 下面是下载图片的


class CaipiaoPipeline_img(ImagesPipeline):
    # 发送请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_src'], meta={'item': item})
    # 文件路径处理

    def file_path(self, request, response=None, info=None, *, item=None):
        # 需要返回文件路径
        item = request.meta['item']
        file_name = item['img_src'].split('/')[-1]
        # print(file_name)
        return file_name
    # 下载完成后的处理

    def item_completed(self, results, item, info):
        # print(results)
        print('下载完成', results[0][1]['path'])
        return item
