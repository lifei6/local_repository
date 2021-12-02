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
N = 128
f1_true = 0.3
f2_true = 0.32
# 设置AR模型的阶数k
k = int(N / 3)
count = 1000

# 存放f1和f2的MSE列表
MSE_f1_list = []
MSE_f2_list = []
SNR_list = []


# 加入不同方差的噪声
def sig_wn(sigma):
    # 存放加入噪声后的信号
    xn_list = []
    for n in range(1, N + 1):
        xn = 10 * sin(2 * pi * f1_true * n + pi / 3) + 2 * sin(2 * pi * f2_true * n + pi / 4) + \
             np.random.normal(0, sigma, 1)[0]
        xn_list.append(xn)
    return xn_list


def burg(xn_list):
    # 数据初始化0阶前向误差和0阶反向误差
    fO = xn_list[:]
    bO = xn_list[:]
    # 用于更新的误差变量
    f = xn_list[:]
    b = xn_list[:]
    # 系数矩阵
    a = np.array(np.zeros((k + 1, k + 1)))
    for i in range(k + 1):
        a[i][0] = 1
    # 计算P0 1/N*sum(xn_list*2)
    P0 = 0
    for i in range(N):
        P0 += xn_list[i] ** 2
    P0 /= N
    P = [P0]
    # Burg 算法更新模型参数
    for p in range(1, k + 1):
        Ka = 0  # 反射系数的分子
        Kb = 0  # 反射系数的分母
        for n in range(p, N):
            Ka += f[n] * b[n - 1]
            Kb = Kb + f[n] ** 2 + b[n - 1] ** 2
        K = 2 * Ka / Kb

        # 更新前向误差和反向误差
        fO = f[:]
        bO = b[:]
        for n in range(p, N):
            b[n] = -K * fO[n] + bO[n - 1]
            f[n] = fO[n] - K * bO[n - 1]
        # 更新此时的模型参数
        for i in range(1, p + 1):
            if (i == p):
                a[p][i] = -K
            else:
                a[p][i] = a[p - 1][i] - K * a[p - 1][p - i]
        # 预测误差功率
        P.append((1 - K ** 2) * P[p - 1])
    # 抽取k阶参数
    a_k = []
    for i in range(0, k + 1):
        a_k.append(a[k][i])
    return a_k, sqrt(P[k])


def one_estimate():
    xn_list = sig_wn(1)
    # 调用burg算法
    a_k, G = burg(xn_list)
    # 计算功率谱
    # 计算频响
    w, h = signal.freqz(G, a_k, worN=N)
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


def estimate(sigma):
    # 用于存放同一个sigma的count个样值
    f1_list = []
    f2_list = []
    # 计算count次f
    for i in range(0, count):
        # 1.获取信号
        xn_list = sig_wn(sigma)
        # 调用burg算法
        a_k, G = burg(xn_list)
        w, h = signal.freqz(G, a_k, worN=N)
        Hf = abs(h)
        # print(Hf[:5], '\n', len(Hf))
        PSD = Hf ** 2
        # 估计f1,f2
        c = int((f1_true + f2_true) * N)
        f1_estimate = (np.argmax(PSD[0:c])) / (2 * N)
        f2_estimate = (np.argmax(PSD[c:int(N)]) + c) / (2 * N)
        f1_list.append(f1_estimate)
        f2_list.append(f2_estimate)
    return f1_list, f2_list


# 计算信噪比
def snr(sigma):
    """
    计算sigma下的信噪比snr
    :param sigma: 标准差
    :return: snr的dB形式
    """
    # 1.存放没有噪声的信号
    sn_list = []
    for n in range(1, N + 1):
        sn = 10 * sin(2 * pi * f1_true * n + pi / 3) + 2 * sin(2 * pi * f2_true * n + pi / 4)
        sn_list.append(sn)
    # 2.调用burg算法
    a_k, G = burg(sn_list)
    print(G)
    # 3.求解功率谱和平均功率
    # w为角频率，h为频响
    w, h = signal.freqz(G, a_k, worN=N)
    Hf = abs(h)
    PSD = Hf ** 2
    mean_power = np.sum(PSD)
    # print(mean_power)
    # 4.计算信噪比
    SNR = mean_power/(sigma ** 2)
    snr_db = 10 * log10(SNR)
    return snr_db


def count_mse():
    # 改变sigma从而改变信噪比
    for sigma in np.linspace(50, 0.1, 250):
        # 获取信噪比
        a = snr(sigma)
        SNR_list.append(a)
        # 每个sigma计算count次f
        f1_temp, f2_temp = estimate(sigma)
        # print(f1_temp, '\n', f2_temp)
        # mse随snr变化曲线
        mean_f1 = np.mean(f1_temp)
        mean_f2 = np.mean(f2_temp)
        # 偏差
        bia_f1 = f1_true - mean_f1
        bia_f2 = f2_true - mean_f2
        for z in range(0, count):
            f1_temp[z] = (f1_temp[z] - mean_f1) ** 2
            f2_temp[z] = (f2_temp[z] - mean_f2) ** 2
        # 方差
        var_f1 = np.mean(f1_temp)
        var_f2 = np.mean(f2_temp)
        # MSE
        MSE_f1_list.append(var_f1 + bia_f1 ** 2)
        MSE_f2_list.append(var_f2 + bia_f2 ** 2)
    # 绘制MSE图像
    # 1.创建画布
    fig, axes = plt.subplots(nrows=1, ncols=2)
    # 2.绘制图像
    axes[0].plot(SNR_list, MSE_f1_list, color='m', linestyle='--', label='f1-MSE')
    axes[1].plot(SNR_list, MSE_f2_list, color='c', linestyle='-.', label='f2-MSE')
    # 3.属性设置
    axes[0].set_xlabel('SNR')
    axes[0].set_ylabel('MSE')
    axes[0].set_title('f1的mse随snr变化曲线')
    axes[1].set_xlabel('SNR')
    axes[1].set_ylabel('MSE')
    axes[1].set_title('f2的mse随snr变化曲线')
    # 4.添加网格
    axes[0].grid(True, linestyle='--', alpha=0.5)
    axes[1].grid(True, linestyle='--', alpha=0.5)
    # 5.添加图例
    axes[0].legend(loc='best')
    axes[1].legend(loc='best')
    # 6.显示图片
    plt.show()


if __name__ == '__main__':
    # 进行一次估计绘制功率谱和估计f1和f2
    one_estimate()
    # 计算MSE
    count_mse()