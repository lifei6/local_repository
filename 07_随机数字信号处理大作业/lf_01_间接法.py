# x = 10*sin(2*pi*0.2*n) + 2*sin(2*pi*0.3*n)+vx
# 平稳随机信号功率谱估计
import numpy as np
import matplotlib.pyplot as plt
from math import *

from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# n取值从1到1024
N = 256
f1_true = 0.3
f2_true = 0.35
count = 100
# 存放mse和snr
MSE_f1_list = []
MSE_f2_list = []
SNR_list = []


# x(n)
def signal(n, sigma):
    if n < 1 or n > N:
        return 0
    else:
        return 10*sin(f1_true * 2 * pi * n + pi / 3) + 2 * sin(f2_true * 2 * pi * n + pi / 4) + np.random.normal(0, sigma, 1)[0]


# 估计f1和f2
def one_estimate(sigma):
    R_list = []  # 存放自相关函数序列
    sums = 0
    # 计算自相关
    for i in range(0, N):
        # R(n+m_train)
        for j in range(1, N + 1 - i):
            # 求和得m时刻的自相关
            sums = sums + (signal(j, sigma) * signal(j + i, sigma) / N)
        R_list.append(sums)
        sums = 0
    # 对自相关进行fft变化得功率谱
    x_transfer = np.fft.fft(R_list, N)
    power_spectrum_list = abs(x_transfer)
    # 频率估计
    # 估计f1,f2
    c = int(((f1_true + f2_true) / 2) * N)
    f1 = (np.argmax(power_spectrum_list[0:c])) / N
    f2 = (np.argmax(power_spectrum_list[c:int(N/2)]) + c) / N
    # 2. 绘制功率谱图像
    x = np.linspace(0, N - 1, N, dtype=np.int32)
    y = power_spectrum_list
    plt.plot(x, y)
    plt.title("基于fft的间接法估计f1=%f,f2=%f" % (f1, f2))
    plt.show()


# 定义一个估计f1,f2的函数
def estimate(sigma):
    """
    用于计算count次f
    :param sigma: 指定噪声的标准差
    :return: 返回f1,f2计算列表
    """
    # 用于存放不同sigma的估计值
    f1_list = []
    f2_list = []
    # 计算count次f
    for n in range(0, count):
        R_list = []  # 存放自相关函数序列
        sums = 0
        # 计算自相关
        for i in range(0, N):
            # R(n+m)
            for j in range(1, N + 1 - i):
                # 求和得m时刻的自相关
                sums = sums + (signal(j, sigma) * signal(j + i, sigma) / N)
            R_list.append(sums)
            sums = 0
        # 对自相关进行fft变化得功率谱
        x_transfer = np.fft.fft(R_list, N)
        power_spectrum_list = abs(x_transfer)
        # 频率估计
        # 估计f1,f2
        c = int(((f1_true + f2_true) / 2) * N)
        f1 = (np.argmax(power_spectrum_list[0:c])) / N
        f2 = (np.argmax(power_spectrum_list[c:int(N / 2)]) + c) / N
        f1_list.append(f1)
        f2_list.append(f2)
    return f1_list, f2_list


def snr(sigma):
    """
    计算sigma下的信噪比snr
    :param sigma: 标准差
    :return: snr的dB形式
    """
    x_list = []
    for n in range(1, N + 1):
        # 1.获取每个点
        x = 10 * sin(2 * pi * f1_true * n + pi/3) + 2 * sin(2 * pi * f2_true * n + pi/4)
        x_list.append(x)
    # 2.进行fft变化
    x_transfer = np.fft.fft(x_list, N)
    # 3.计算功率谱和求平均功率
    power_spectrum_list = (abs(x_transfer) ** 2) / N
    mean_power = np.sum(power_spectrum_list)
    # print(mean_power)
    # 4.计算信噪比
    SNR = mean_power/(sigma ** 2)
    snr_db = 10 * log10(SNR)
    return snr_db


def count_mse():
    """
    计算mse
    """
    # 改变sigma从而改变信噪比
    for sigma in np.linspace(200, 1, 50):
        # 每个sigma计算count次f
        a = snr(sigma)
        SNR_list.append(a)
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

    # print('f1的均方根误差', MSE_f1_list)
    # print('f2的均方根误差', MSE_f2_list)
    # (三)绘制MSE
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
    one_estimate(1)
    count_mse()
