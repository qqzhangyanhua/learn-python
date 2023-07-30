# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道想要使用必须在settings.py中开启   
class TutorialPipeline:
    # 管道,处理数据
    def process_item(self, item, spider):
        with open('youxi.csv',mode='a',encoding='utf-8') as f:
            f.write(f'{item["name"]},{item["fenlei"]},{item["create_time"]}\n')
        return item
