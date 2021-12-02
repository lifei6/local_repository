# 要求：用AR模型和yule walker方程进行现代普估计
# 信号：xn = 10*sin(2*pi*0.2*n+pi/3) + 2*sin(2*pi*0.3*n+pi/4)+wn
# 其中f1 = 0.2, f2 = 0.3 ,wn为awgn噪声，1<=n<=1024,共1024个点

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
f1_true = 0.3
f2_true = 0.32
count = 1000
# 设置AR模型的阶数p
p = int(N / 3)
# yule walker方程的个数M，设置为超定方程
M = p + 5
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


# 求自相关
def xcorr(xn_list):
    """
    自相关函数:移位相乘相加
    :param xn_list: 输入信号列表
    :return: R_list
    """
    # 存放自相关函数
    R_list = []
    for m in range(0, N):
        sum = 0
        for n in range(0, N - m):
            sum += (xn_list[n] * xn_list[n + m]) / N
        R_list.append(sum)
    return R_list


# yule-walker求解p+1个参数
def yule_walker_ls(R_list):
    """
    构造yule walker方程，使用最小二乘法求解
    :param R_list: 自相关列表
    :return: AR模型的p+1个参数
    """
    # RA = -B
    # 求系数矩阵（M*p）
    R = np.zeros((M, p))
    for i in range(0, M):
        for j in range(0, p):
            R[i][j] = R_list[abs(i - j)]
    B = np.zeros(M)
    for i in range(1, M + 1):
        B[i - 1] = R_list[i]
    # 转为列向量
    B = B.T
    # 采用LS方法求解方程
    RT = R.T
    RT_R = np.dot(RT, R)
    RT_R_inv = np.linalg.inv(RT_R)
    # A存放估计的系数的列向量
    A = -np.dot(np.dot(RT_R_inv, RT), B)
    # A转为行向量
    A = A.T
    # 加入a0
    A = np.insert(A, 0, 1)
    # 估计G
    G = 0
    for i in range(0, len(A)):
        G += R_list[i] * A[i]
    G = np.sqrt(G)
    return A, G


# 进行一次估计绘制功率谱
def one_estimate():
    """
    估计一次f1和f2并且绘制功率谱
    """
    # 1.获取信号
    xn_list = sig_wn(1)
    # 2.求自相关
    R_list = xcorr(xn_list)
    # 3.求AR模型的参数
    A, G = yule_walker_ls(R_list)
    # 求解功率谱
    # w为角频率，h为频响
    w, h = signal.freqz(G, A, worN=N)
    Hf = abs(h)
    # print(Hf[:5], '\n', len(Hf))
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
    plt.title('yule-walker方程f1=%0.3f f2=%0.3f' % (f1_estimate, f2_estimate), fontsize=20)
    plt.legend()
    plt.show()


# 估计f1和f2
def estimate(sigma):
    """
    进行f1和f2的估计，每估计一次在列表中生成一个样值
    :param sigma: 噪声标准差
    :return: 以列表形式返回count个样值
    """
    # 用于存放同一个sigma的count个样值
    f1_list = []
    f2_list = []
    # 计算count次f
    for i in range(0, count):
        # 1.获取信号
        xn_list = sig_wn(sigma)
        # 2.求自相关
        R_list = xcorr(xn_list)
        # 3.求AR模型的参数
        A, G = yule_walker_ls(R_list)
        # 4.求解功率谱
        # w为角频率，h为频响
        w, h = signal.freqz(G, A, worN=N)
        Hf = abs(h)
        PSD = Hf ** 2
        # 5.估计f1,f2
        c = int((f1_true + f2_true) * N)
        # print(c)
        f1_estimate = (np.argmax(PSD[0:c])) / (2 * N)
        f2_estimate = (np.argmax(PSD[c:int(N)]) + c) / (2 * N)
        # print(f1_estimate, f2_estimate)
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
    # 2.用yule walker方程和AR模型求频谱
    R_list = xcorr(sn_list)
    A, G = yule_walker_ls(R_list)
    # 3.求解功率谱和平均功率
    # w为角频率，h为频响
    w, h = signal.freqz(G, A, worN=N)
    Hf = abs(h)
    PSD = Hf ** 2
    mean_power = np.sum(PSD)
    # print(mean_power)
    # 4.计算信噪比
    SNR = mean_power / (sigma ** 2)
    snr_db = 10 * log10(SNR)
    return snr_db


def count_mse():
    """
    计算mse
    """
    # 改变sigma从而改变信噪比
    for sigma in np.linspace(200, 0.1, 500):
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
    # 进行一次估计以及功率谱的绘制
    one_estimate()
    # 绘制mse图像
    count_mse()
