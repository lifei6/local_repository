# 爬取免费简历模板：https://sc.chinaz.com/jianli/free.html
import requests
from lxml import etree
import os
if __name__ == '__main__':
    # 1.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 2.指定页面url
    url = 'https://sc.chinaz.com/jianli/free.html'
    # 3.获取页面源码数据
    response = requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    page_text = response.text
    # 4.解析出每个模板的href属性（详情页的url）和 模板名称
    tree = etree.HTML(page_text)
    # 5.获取全部div标签
    div_list = tree.xpath('//div[@id="main"]/div/div')
    # 6.创建一个用于存放简历的文件夹
    if not os.path.exists('./jianliLibs'):
        os.mkdir('./jianliLibs')
    for div in div_list[:5]:
        # 局部解析出详情页的url和名称
        detail_url = 'https:' + div.xpath('./a/@href')[0]
        name = div.xpath('./p/a/text()')[0]
        # name = name.encode('iso-8859-1').decode('gbk')
        print(detail_url,name,'\n')
        # 进行详情页数据获取
        detail_text = requests.get(url=detail_url,headers=headers).text
        # 进行下载地址解析--采用广东电信下载
        tree = etree.HTML(detail_text)
        down_load_url = tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li[3]/a/@href')[0]

        # 进行二进制数据下载
        data = requests.get(url=down_load_url,headers=headers).content
        # 数据持久化存储
        # 文件路径
        name_path = './jianliLibs/' + name + '.rar'
        with open(name_path,'wb') as fp:
            fp.write(data)
        print(name,'下载成功')
    print('over!!!')
