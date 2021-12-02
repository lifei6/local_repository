import requests
import json
if __name__ == '__main__':
    # 1.指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # 2.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 3.指定参数
    data = {
        'cname': '',
        'pid': '',
        'keyword': '长沙',
        'pageIndex': '2',
        'pageSize': '10'
    }
    # 4.发起请求
    response = requests.post(url=url,data=data,headers=headers)
    # 5.获取数据
    dic_text = response.text
    print(dic_text)
    # 6.数据持久化
    with open('./kendeji.text','w',encoding='utf-8') as fp:
        fp.write(dic_text)
    print('over!!!')