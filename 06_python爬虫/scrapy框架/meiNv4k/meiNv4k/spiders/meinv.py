import scrapy
from meiNv4k.items import Meinv4KItem

class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']
    # 生成一个通用的url模板(不可变)
    url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    page_num = 2
    def parse(self, response):
        li_lsit=response.xpath('//*[@id="main"]/div[3]/ul/li')
        all_data = []
        for li in li_lsit:
            # 解析图片名称
            name = li.xpath('./a/b/text()')[0].extract()
            print(name)

            item = Meinv4KItem()
            item['name'] = name

            # 将item提交管道
            yield item

        # 设置解析的页面数
        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num+=1
            # 手动发起请求：callback回调函数专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)


