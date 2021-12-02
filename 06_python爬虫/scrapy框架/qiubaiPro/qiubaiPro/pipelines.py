# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiproPipeline:
    fp =None
    # 重写父类的一个方法:改方法只会在刚开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始爬虫...')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    # 专门用来处理item类型的对象
    # 改方法可以接收爬虫文件提交过来的item对象
    # 改方法没接收到一个item对象就会调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author+':'+content+'\n')
        return item

    # 改方法只会在爬虫结束的时候调用一次
    def close_spider(self,spider):
        print('爬虫结束...')
        self.fp.close()