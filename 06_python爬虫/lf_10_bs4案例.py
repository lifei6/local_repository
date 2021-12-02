import requests
from bs4 import BeautifulSoup
import lxml
# 爬取三国演义小说中的所有章节标题和章节内容
# https://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 指定url
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # 获取页面源码数据
    page_text = requests.get(url=url,headers=headers).text.encode('ISO-8859-1')
    # 使用bs4解析出章节标题和章节详情页的url
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    # print(li_list)
    # 打开一个储存数据的文本
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        # 获取章标题
        title = li.a.string
        # 获取章节详情页url
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        # 获取详情页数据-章节数据
        detail_page_text = requests.get(url=detail_url,headers=headers).text.encode('ISO-8859-1')
        # 解析详情页数据
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        content = detail_soup.find('div',class_='chapter_content').text
        # 数据持久化
        fp.write(title+':'+content+'\n')
        print(title,'保存成功')
    print('爬取结束')


