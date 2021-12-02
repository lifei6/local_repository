# 1.导入多进程模块
import multiprocessing
import os
import time


def dance():
    # 获取子进程id2
    id2 = os.getpid()
    print("dance子进程的id:",id2)
    # 获取父进程id
    print("dance的父进程id：", os.getppid())
    # 获取进程名
    print("dance的进程名：",multiprocessing.current_process())
    for i in range(5):
        time.sleep(1)
        print('跳舞',i)


def sing():
    # 获取子进程id3
    id3 = os.getpid()
    print("sing子进程的id:", id3)
    # 获取父进程id
    print("sing的父进程id：",os.getppid())
    for i in range(5):
        time.sleep(1)
        print('唱歌',i)

if __name__ == '__main__':
    # 注意点：！！！
    # 三个进程：一个主进程，两个子进程
    # 三个线程：每个进程一个线程（进行任务的）
    # 获取进程id
    id1 = os.getpid()
    print("主进程的id:",id1)
    # 2.创建子进程
    # Process(target) target:指定执行的任务名(函数名)
    # name:给子进程起名
    my_dance = multiprocessing.Process(target=dance, name='my_process1')
    my_sing = multiprocessing.Process(target=sing, name='my_process2')

    # 3.开始子进程
    my_sing.start()
    my_dance.start()