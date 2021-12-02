# 进行美女图片爬取
import requests
from lxml import etree
import os
if __name__ == '__main__':
    # 1.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 2.指定页面url
    url = 'https://pic.netbian.com/4kmeinv/'
    # 3.获取页面源码数据
    response = requests.get(url=url,headers=headers)
    # # 手动修改数据编码
    # response.encoding = 'utf-8'
    page_text = response.text
    # 4.进行数据解析获取图片的src和alt属性
    tree = etree.HTML(page_text)
    # 获取li标签列表
    li_list = tree.xpath('//div[@class="slist"]//li')
    # 创建一个保存图片的文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        # 进行局部解析，获取图片src
        img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        # 进行局部解析，获取图片名称
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用的一种修改乱码的方式
        img_name =img_name.encode('iso-8859-1').decode('gbk')
        # 对图片的src发起请求，获取图片数据
        img_data = requests.get(url=img_src,headers=headers).content
        # 图片地址
        img_path = './picLibs/' + img_name
        # 保存图片
        with open(img_path,'wb') as fp:
            fp.write(img_data)
        print(img_name,'保存成功')


