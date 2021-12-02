import asyncio

async def requests(url):
    print("正在发起请求",url)
    print("请求成功",url)
    return url

# async修饰的函数，调用之后返回一个协程对象
c = requests('www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# # task的使用
# loop = asyncio.get_event_loop()
# # 基于loop创建了一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# # future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# 绑定回调
def callback_func(task):
    # result返回的就是任务对象中封装的协程对象对应的函数返回值
    print(task.result())
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
task.add_done_callback(callback_func)
loop.run_until_complete(task)
