import requests
import json
if __name__ == '__main__':
    # 1.指定url
    url = 'https://movie.douban.com/j/chart/top_list?'
    # 2.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 3.指定参数
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 指定抓取电影开始的位置
        'limit': '20'
    }
    # 4.发起请求
    response = requests.get(url=url,params=param,headers=headers)
    # 5.获取数据
    list_data = response.json()
    # 6.数据持久化
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp,ensure_ascii=False)
    print('over!!!')