import requests
import json
if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 3.设置post请求参数
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 4.发起请求设置参数
    response = requests.post(url=post_url,data=data,headers=headers)
    # 5. 获取数据:json()方法返回的是obj,得确定获取的数据是json,否则会报错
    # 可以通过抓包工具去看content_type
    dic_obj = response.json()
    print(dic_obj)
    # 6.数据持久化
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp,ensure_ascii=False)
    print('over!!!')