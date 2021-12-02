# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter


# class MeinvimgproPipeline:
#     fp = None
#
#     # 重写父类的一个方法:改方法只会在刚开始爬虫的时候调用一次
#     def open_spider(self, spider):
#         print('开始爬虫...')
#         self.fp = open('./meinvimgLib.txt', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         name = item['name']
#         self.fp.write(name + '\n')
#         return item
#
#     # 改方法只会在爬虫结束的时候调用一次
#     def close_spider(self, spider):
#         print('爬虫结束...')
#         self.fp.close()


#导包
from scrapy.pipelines.images import ImagesPipeline
import scrapy
# 基于ImagesPipeline的自定义管道类
class imagesPipLine(ImagesPipeline):
    # 就是根据图片地址进行请求
    def get_media_requests(self, item, info):
        # 手动请求
        yield scrapy.Request(url=item['src'])
    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        # imgName = item['name']
        return imgName
    def item_completed(self, results, item, info):
        # 返回给下一个即将执行的管道类
        return item
