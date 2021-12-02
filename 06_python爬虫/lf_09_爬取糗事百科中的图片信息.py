# 正则解析
import requests
import json
import re
import os
if __name__ == '__main__':
    # # 1.如何爬取图片
    # url = 'https://pic.qiushibaike.com/system/pictures/12461/124619938/medium/190FSYX3N55C2LFE.jpg'
    # # content返回的是二进制形式的图片数据
    # # text(字符串)，json（）(对象)，content(二进制)
    # img_data = requests.get(url=url).content
    # with open('./qiutu.jpg','wb') as fp:
    #     fp.write(img_data)
    # print('over！！！')
    # 创建保存图片的文件夹
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # 1.设置一个通用的url模板
    for page in range(1,6):
        url = 'https://www.qiushibaike.com/imgrank/%d/'
        url = format(url%page)
        # 2.UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }
        # 3.发起请求
        page_text = requests.get(url=url,headers=headers).text
        # 4.使用聚焦爬虫对页面中所有糗图进行解析提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)
        for img_src in img_src_list:
            # 进行拼接成一个完整的图片url
            src = 'https:'+img_src
            # 请求获取图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            # 对图片进行存储
            # 1.生成图片名称
            img_name = src.split('/')[-1]
            # 2.生成图片地址
            imgPath = './qiutuLibs/' + img_name
            # 3.保存图片
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
            print(img_name,'保存成功')
