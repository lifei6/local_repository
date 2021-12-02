# 爬取搜狗首页的页面数据
import requests

if __name__ == '__main__':
    # 1.指定url
    url = 'https://www.sogou.com/'
    # 2.发起请求
    # get返回的是一个响应对象
    response = requests.get(url=url)
    # 3.获取数据
    page_text = response.text
    print(page_text)
    # 4.持久化存储
    with open('./sogou.html', 'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')