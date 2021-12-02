# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BossproPipeline:
    fp = None

    # 重写父类的一个方法:改方法只会在刚开始爬虫的时候调用一次
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./boss.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        job_name = item['job_name']
        job_detail = item['job_detail']
        self.fp.write(job_name+':'+job_detail+'\n')
        return item

    # 改方法只会在爬虫结束的时候调用一次
    def close_spider(self,spider):
        print('爬虫结束...')
        self.fp.close()
