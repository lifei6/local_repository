# UA:User-Agent(请求载体的身份识别)
# UA检测：反爬，看你是正常浏览器还是基于爬虫
# UA伪装：反反爬：将身份伪装为浏览器
import requests
if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 1.指定url
    url = 'https://www.sogou.com/sogou?'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 2.url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url,params=param,headers=headers)
    # 3.获取数据
    page_text = response.text
    # 4.持久化存储
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')

