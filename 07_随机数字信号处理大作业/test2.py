import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import signal

from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 定义全局参数
N = 256
f1_true = 0.1
f2_true = 0.3
count = 100
# 设置AR模型的阶数p
p = int(N / 2)


# 加入不同方差的噪声
def sig_wn(sigma):
    # 存放加入噪声后的信号
    xn_list = []
    for n in range(1, N + 1):
        xn = 10 * sin(2 * pi * f1_true * n + pi / 3) + 2 * sin(2 * pi * f2_true * n + pi / 4) + \
             np.random.normal(0, sigma, 1)[0]
        xn_list.append(xn)
    return xn_list


def one_estimate():
    xn_list = sig_wn(0.5)
    # 1.计算预测误差功率的初始值P0
    # 存放预测误差功率
    P = []
    sum = 0
    for i in range(0, N):
        sum += xn_list[i] ** 2
    P0 = sum / N
    P.append(P0)
    # 2.定义前向预测误差和后向预测误差的初始值
    fpe = np.zeros((p + 1, N))
    bpe = np.zeros((p + 1, N))
    # 0阶预测误差
    fpe[0] = xn_list
    bpe[0] = xn_list
    # print(fpe[0].shape)
    # 3.递推求各阶反射系数
    Km = []
    for m in range(1, p + 1):
        # 反射系数的分子和分母
        Ka = 0
        Kb = 0
        for n in range(m, N):
            Ka += fpe[m - 1][n - 1] * bpe[m - 1][n - 2]
            Kb += (fpe[m - 1][n - 1] ** 2 + bpe[m - 1][n - 2] ** 2) / 2
        # 反射系数
        K = -Ka / Kb
        Km.append(K)
        # 递推前向预测误差和后向预测误差
        for n in range(m, N):
            fpe[m][n - 1] = fpe[m - 1][n - 1] + Km[m - 1] * bpe[m - 1][n - 2]
            bpe[m][n - 1] = Km[m - 1] * fpe[m - 1][n - 1] + bpe[m - 1][n - 2]
        # 误差平均功率
        P.append((1 - Km[m - 1] ** 2) * P[m - 1])
    print(fpe[:5, :5])
    print((bpe[:5,:5]))
    # 4.模型参数初始化
    a = np.zeros((p, p))
    # 把频率响应分子当作1
    G = 1
    # 初始化一阶初始值
    a[0][0] = Km[0]
    # 5.把各阶反射系数带入levinson递推公式进行迭代
    # 递推得到p阶的参数a[p]
    for m in range(2, p + 1):
        # 计算a(1)到a(m-1)
        for n in range(1, m):
            a[m - 1][n - 1] = a[m - 2][n - 1] + Km[m - 1] * a[m - 2][m - 1 - (n - 1)]
        # 计算a(m)
        a[m - 1][m - 1] = Km[m - 1]
    # 6.抽取p阶参数
    a_p = []
    # 添加a(0)
    a_p.append(0)
    for i in range(0, p):
        a_p.append(a[p - 1][i])
    print(len(a_p))

    # 7.计算功率谱
    # 计算频响
    w, h = signal.freqz(G, a_p, worN=N)
    Hf = abs(h)
    PSD = Hf ** 2
    f = w / (2 * pi)
    # 估计f1,f2
    c = int((f1_true + f2_true) * N)
    f1_estimate = (np.argmax(PSD[0:c])) / (2 * N)
    f2_estimate = (np.argmax(PSD[c:int(N)]) + c) / (2 * N)
    # print(f1_estimate, f2_estimate)
    # 绘制功率谱
    plt.plot(f, PSD, color='c', label='功率谱线')
    plt.xlabel('频率（f）')
    plt.ylabel('功率谱（PSD）')
    plt.title('Burg算法：f1=%0.3f f2=%0.3f' % (f1_estimate, f2_estimate), fontsize=20)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    one_estimate()

