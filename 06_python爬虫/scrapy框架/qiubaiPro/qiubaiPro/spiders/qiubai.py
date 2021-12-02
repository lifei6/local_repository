import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     # 解析：作者的名称+段子的内容
    #     # xpath返回的是列表，但列表元素一定是Selector类型的对象
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     # 存放所有数据的列表
    #     all_data =[]
    #     for div in div_list:
    #         # extract()可以将selector对象中的data参数存储的字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         # 列表加extract可以直接将列表中的每个selectord的data内容提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         # 列表转字符串
    #         content = "".join(content)
    #         # 存放一组数据的字典
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        # 解析：作者的名称+段子的内容
        # xpath返回的是列表，但列表元素一定是Selector类型的对象
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        # 存放所有数据的列表
        all_data =[]
        for div in div_list:
            # extract()可以将selector对象中的data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            # 列表加extract可以直接将列表中的每个selectord的data内容提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            # 列表转字符串
            content = "".join(content)

            # 实例化一个item对象
            item = QiubaiproItem()
            item['author']=author
            item['content']=content

            # 将item提交给管道
            yield item
