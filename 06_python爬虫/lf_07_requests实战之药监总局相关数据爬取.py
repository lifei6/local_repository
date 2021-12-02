import requests
import json
if __name__ == '__main__':
    # 首页的url:-get-无id-http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList
    # post-有id-http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList
    # 详情页url: post-http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    id_list = [] # 用于存放所有公司的id
    all_data_list = [] # 用于存放企业详情
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # 1.批量获取不同企业的id
    for page in range(1,6):
        page = str(page)
        # 1.1指定首页的post_url
        url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
        # 1.2设置参数
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        # 1.3发起请求
        json_ids = requests.post(url=url,data=data,headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    # print(id_list)
    # 2.获取企业详情
    # 2.1 指定post_url
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    # 2.2 设置参数
    for id in id_list:
        data = {
            'id': id
        }
        # 2.3发起请求获取详情
        detail_data = requests.post(url=post_url,data=data,headers=headers).json()
        # print(detail_data)
        all_data_list.append(detail_data)
    # 3.持久化保存
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp,ensure_ascii=False)
    print('over!!!')


