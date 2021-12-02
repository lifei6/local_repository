# 任务：
# 信号：x = 10*sin(2*pi*0.2*n+pi/3) + 2*sin(2*pi*0.3*n+pi/4)+vx
# 其中f1 = 0.2, f2 = 0.3 ,vx为awgn噪声，1<=n<=1024,共1024个点
# 求：（一）x的功率谱密度power_spectrum_list,绘制功率谱图
#    （二）估计f1和f2
#    （三）画出不同信噪比(SNR)下估计结果的均方根误差MES

import numpy as np
from matplotlib import pyplot as plt
from math import *

from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 设置点数
N = 256
# 设置频率
f1_true = 0.3
f2_true = 0.32
# 设置计算次数
count = 500

# 存放mse和snr
MSE_f1_list = []
MSE_f2_list = []
SNR_list = []


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


def one_esimate():
    # 1.信号取值
    # 定义两个存放信号的列表（幅值和变换后的数字频率k）
    fs = 1
    x_list = []
    k = []
    for n in range(1, N + 1):
        x = 10 * sin(2 * pi * f1_true * n + pi/3) + 2 * sin(2 * pi * f2_true * n + pi/4) + \
            np.random.normal(0, 1, 1)[0]
        x_list.append(x)
        k.append(n * fs / N)
    # 2.进行fft变化
    x_transfer = np.fft.fft(x_list, N)
    # 3.计算功率谱
    power_spectrum_list = (abs(x_transfer) ** 2) / len(x_list)
    # 4.频率估计
    # 估计f1,f2
    c = int(((f1_true + f2_true) / 2) * N)
    f1 = (np.argmax(power_spectrum_list[0:c])) / N
    f2 = (np.argmax(power_spectrum_list[c:int(N/2)]) + c) / N
    print('f1:%.2f, f2:%.2f' % (f1, f2))
    # 5.绘制功率谱
    plt.plot(k, power_spectrum_list, color='c', label='功率谱线')
    plt.xlabel('数字频率（k）')
    plt.ylabel('功率谱（PSD）')
    plt.title('采用基于fft的直接法谱估计:f1=%.2f f2=%.2f' % (f1, f2), fontsize=20)
    plt.legend()
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
    for i in range(0, count):
        # 1.信号取值
        x_list = []
        for n in range(1, N + 1):
            x = 10*sin(2*pi*f1_true*n + pi/3) + 2*sin(2*pi*f2_true*n + pi/4)+np.random.normal(0, sigma, 1)[0]
            x_list.append(x)
        # 2.进行fft变化
        x_transfer = np.fft.fft(x_list, N)
        # 3.计算功率谱
        power_spectrum_list = (abs(x_transfer)**2)/len(x_list)
        # 4.频率估计
        # 估计f1,f2
        c = int(((f1_true + f2_true)/2) * N)
        f1 = (np.argmax(power_spectrum_list[0:c])) / N
        f2 = (np.argmax(power_spectrum_list[c:int(N)]) + c) / N
        # (二)print('f1:%f, f2:%f' % (f1, f2))
        f1_list.append(f1)
        f2_list.append(f2)
    return f1_list, f2_list


def count_mse():
    """
    计算mse
    """
    # 改变sigma从而改变信噪比
    for sigma in np.linspace(200, 1, 200):
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
    # 为了画出功率谱图只进行一次估计
    one_esimate()
    # 计算MSE
    count_mse()


