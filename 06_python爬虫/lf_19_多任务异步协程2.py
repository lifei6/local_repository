import requests
import asyncio
import time
import aiohttp
import os
# 爬取三个网页的页面数据
# session是异步协程的请求模块
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
if not os.path.exists('./yibupaquLibs'):
    os.mkdir('./yibupaquLibs')

# async修饰函数，调用后返回协程对象
async def requests(url):
    async with aiohttp.ClientSession() as session:
        # 如果要进行代理IP,用proxy
        # 带参数 用params/data
        print('正在发起请求',url)
        async with await session.get(url=url, headers=headers) as response:
            # text(), reas(), json()
            page_text = await response.text()
            path_name = './yibupaquLibs/' + url.split('.')[1] + '.html'
            with open(path_name,'w',encoding='utf-8') as fp:
                fp.write(page_text)
                print('请求成功')

start = time.time()
urls = ['https://www.sogou.com/',
        'https://www.baidu.com/?tn=48021271_38_hao_pg',
        'https://movie.douban.com/']
# 存放多任务的列表
tasks = []
for url in urls:
    c = requests(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('耗时：', time.time() - start)