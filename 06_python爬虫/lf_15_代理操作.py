import requests

if __name__ == '__main__':
    ip_url = 'https://www.baidu.com/s?word=ip'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 代理
    proxies = {'http': '183.247.202.208:30001'}
    page_text = requests.get(url=ip_url,headers=headers,proxies=proxies).text
    with open('./ip.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
