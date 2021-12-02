import asyncio
import time

async def requests(url):
    print("请求发起",url)
    # 在异步协程中如果出现同步模块的代码，那么就无法实现异步
    # time.sleep(2)
    # 当asyncio遇到阻塞操作时必须手动挂起
    await asyncio.sleep(2)
    print("请求成功",url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.douban.com',
    'www.goubanjia.com'
]
# 用于存放任务列表
stasks = []
for url in urls:
    c = requests(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
loop = asyncio.get_event_loop()
# 固定用法，需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print("执行用时",time.time() - start)