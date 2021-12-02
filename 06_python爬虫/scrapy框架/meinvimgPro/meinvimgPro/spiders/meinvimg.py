import scrapy
from meinvimgPro.items import MeinvimgproItem

class MeinvimgSpider(scrapy.Spider):
    name = 'meinvimg'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']
    # 生成一个通用的url模板(不可变)
    url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    page_num = 2

    def parse(self, response):
        li_lsit = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_lsit:
            # 解析图片名称
            name = li.xpath('./a/b/text()')[0].extract()
            # 解析图片的src：注意可能有伪属性，全换成src2(这里没有)
            img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0].extract()
            # print(img_src)

            item = MeinvimgproItem()
            item['name'] = name
            item['src'] = img_src
            # 将item提交管道
            yield item

        # 设置解析的页面数
        if self.page_num <= 10:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动发起请求：callback回调函数专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
