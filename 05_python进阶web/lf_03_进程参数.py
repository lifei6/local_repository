# 1.导入多进程模块
import multiprocessing
import os
import time

# 带有参数的函数
def dance(count):
    for i in range(count):
        time.sleep(1)
        print('跳舞',i)


if __name__ == '__main__':
    # 2.创建子进程
    # Process(target) target:指定执行的任务名(函数名)
    # name:给子进程起名
    # args:元组!!!(单个元素的元组有,)
    my_dance = multiprocessing.Process(target=dance, name='my_process1',args=(5,))

    # 3.开始子进程
    my_dance.start()