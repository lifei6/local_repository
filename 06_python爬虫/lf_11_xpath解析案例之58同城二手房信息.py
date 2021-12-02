import requests
from lxml import etree
# 获取58同城二手房的房源信息
if __name__ == '__main__':
    # 1.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 2.指定页面url
    url = 'https://chenzhou.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0163-fbe1-9f5a-772aa38e597a&ClickID=6'
    # 3.获取页面源码信息
    page_text = requests.get(url=url,headers=headers).text
    # 4.xpath进行数据解析
    tree = etree.HTML(page_text)
    # 获取div标签列表
    div_list = tree.xpath('//section[@class="list"]/div')
    print(div_list)
    # 创建一个存储房源信息的文件
    fp = open('./ershoufang.txt','w',encoding='utf-8')
    for div in div_list:
        # 进行局部解析，获取标题
        title = div.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        # 进行局部解析，获取价格
        price_data_list = div.xpath('.//p[@class="property-price-total"]/span/text()')
        price = ''.join(price_data_list)
        # 持久化存储
        fp.write(title + ':' + price + '\n')
        print(title,'爬取成功')