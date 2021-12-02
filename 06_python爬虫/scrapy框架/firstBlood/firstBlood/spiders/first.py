import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称：就是爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名: 用来限定start_urls中哪些url可以发起请求
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表：该列表中存放的url会自动的被scrapy请求发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com']

    # 用作于数据解析：response参数表示的是请求成功后的响应对象
    def parse(self, response):
        print(response)
