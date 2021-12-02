import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101180100&industry=&position=']
    # # 定义一个url模板
    url = 'https://www.zhipin.com/c101180100/?query=python&page=%d'
    page_num = 2

    # 详情页的数据解析方法
    # 回调函数接收item
    def detail_parse(self,response):
        item=response.meta['item']
        job_detail =response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_detail = "".join(job_detail)
        item['job_detail']=job_detail
        yield item

    def parse(self, response):
        # 数据解析
        li_list = response.xpath('/body/div/div[3]/div/div[3]/ul/li')
        for li in li_list:
            # 解析岗位名称
            job_name = li.xpath('.//*[@class="job-name"]/a/@title')[0].extract()

            # 封装为item
            item = BossproItem()
            item['job_name'] = job_name

            # 解析详情数据的url
            detail_url ='https://www.zhipin.com' + li.xpath('.//*[@class="job-name"]/a/@href')[0].extract()

            # 手动发起请求
            # 请求传参：meta={},可以将meta字典传递给回调函数
            yield scrapy.Request(detail_url, callback=self.detail_parse,meta={'item': item})

            # 分页操作
            if self.page_num<=10:
                new_url = format(self.url%self.page_num)
                self.page_num+=1
                yield scrapy.Request(url=new_url,callback=self.parse)
