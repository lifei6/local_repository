import requests
from lxml import etree
# 爬取全国城市名称；https://www.aqistudy.cn/historydata/
if __name__ == '__main__':
    # 1.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 2.指定页面url
    url = 'https://www.aqistudy.cn/historydata/'
    # 3.进行页面源码数据获取
    page_text = requests.get(url=url,headers=headers).text
    # 4.进行数据解析，获取热门城市和全国城市的名称
    tree = etree.HTML(page_text)
    # hot: //div[@class="bottom"]/ul/li/a
    # normal: //div[@class="bottom"]/ul/div[2]/li/a
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_list = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_list.append(city_name)
    print(all_city_list,'\n',len(all_city_list))