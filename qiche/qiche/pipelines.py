
import pymysql


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QichePipeline:
    def open_spider(self, spider):
        print('sql建立连接===')
        self.conn = pymysql.connect(
            user='root',
            password='admin123',
            host='localhost',
            database='crawl',
        )

    def close_spider(self, spider):
        print('爬虫结束了sql')
        self.conn.close()

    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = 'insert into qiche(title,price,url) values(%s,%s,%s)'
            cursor.execute(
                sql, (item['title'], (item['price']), item['url']))
            self.conn.commit()
            print('存储数据1条')
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
