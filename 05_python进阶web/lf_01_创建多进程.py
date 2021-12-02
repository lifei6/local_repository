# 1.导入多进程模块
import multiprocessing
import time


def dance():
    for i in range(5):
        time.sleep(1)
        print('唱歌',i)


def sing():
    for i in range(5):
        time.sleep(1)
        print('跳舞',i)
if __name__ == '__main__':
    # 注意点：！！！
    # 三个进程：一个主进程，两个子进程
    # 三个线程：每个进程一个线程（进行任务的）
    # 2.创建子进程
    # Process(target) target:指定执行的任务名(函数名)
    # name:给子进程起名
    my_dance = multiprocessing.Process(target=dance,name='my_process1')
    my_sing = multiprocessing.Process(target=sing,name='my_process2')

    # 3.开始子进程
    my_sing.start()
    my_dance.start()