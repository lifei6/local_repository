import numpy as np
# from matplotlib import pyplot as plt
import pandas as pd
# from math import *
# import time


from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False


# 1.构造数据集
# 2.数据集划分
# 3.模型假设
# 4.采用梯度下降算法进行参数更新，设置好迭代次数
# 5.模型评估与预测


# 归一化函数
def normalization(positive_data, negative_data):
    """
    归一化函数
    :param positive_data: 正例数据
    :param negative_data: 反列数据
    :return: 归一化后的正反例数据
    """
    # 2.数据预处理--归一化处理
    all_data = pd.concat([positive_data, negative_data], join='inner', axis=0)
    sum_data = all_data.iloc[:, :-1].sum(axis=1)
    # 归一化后的特征值数据
    x_std_data = all_data.iloc[:, :-1].div(sum_data, axis=0)
    new_data = pd.concat([x_std_data, all_data[all_data.columns[-1]]], join='outer', axis=1)
    std_positive_data = new_data.iloc[0:positive_data.shape[0], :]
    std_negative_data = new_data.iloc[positive_data.shape[0]:, :]
    # print(std_positive_data, '\n', std_negative_data)
    return std_positive_data, std_negative_data


# 梯度下降算法
def gradient_descend_method(m_train, d_train, x_train, y_train, alpha, iteration):
    """
    梯度下降去优化目标函数
    这里的目标函数是由sigmoid推出来的
    :param m_train: 训练集样本个数
    :param d_train: 训练集特征值个数
    :param x_train: 训练集特征值
    :param y_train: 训练集目标值
    :return: 模型的参数d+1个
    """
    # beta随机初始化d+1个未知数
    beta = np.random.randn(d_train + 1).T
    # 外循环j控制迭代次数，内循环n变例所以训练集样本
    for j in range(0, iteration):
        # beta初始化d+1个未知数
        beta_T = beta.T
        # print(beta_T)
        # 构造优化函数
        l_beta = 0
        a = 0
        # 遍历样本取得x,y
        for n in range(0, m_train):
            # x列向量
            x = np.insert(x_train[n], len(x_train[n]), 1).T
            # y标量
            y = y_train[n]
            beta_T_x = np.dot(beta_T, x)
            # l_beta待优化函数
            l_beta += -y * beta_T_x + np.log(1 + np.exp(beta_T_x))
            # a为偏导数列向量
            a += -np.dot(x, (y - np.exp(beta_T_x) / (1 + np.exp(beta_T_x))))
        # 采用梯度下降算法求最优解 w = w - alpha*(优化函数对w的一阶偏导数a)
        # if j < 5 or j > iteration - 5:
        #     print("待优化函数的值为", l_beta)
        beta = beta - alpha * a
        # time.sleep(0.5)
    # print("最终的beta", beta)
    return beta


# sigmoid预测模型
def model(x, beta):
    """
    构造sigmoid模型，并对测试集预测
    :param x: 测试集的每个样本的特征值
    :param beta: 梯度下降得到的参数
    :return: 返回预测值
    """
    # 4.模型构造z = w.T*x +b作为sigmoid函数的自变量
    w_T = beta.T[:-1]
    b = beta.T[-1]
    z = np.dot(w_T, x) + b
    y = 1 / (1 + np.exp(-z))
    if y > 0.5:
        y_label = 1
    else:
        y_label = 0
    return y_label


if __name__ == '__main__':
    # 设置学习率
    alpha = 0.05
    # 设置迭代次数
    iteration = 1000
    # 1.构造数据集
    positive_data = pd.DataFrame(
        data=[[0.697, 0.460, 1], [0.774, 0.376, 1], [0.634, 0.264, 1], [0.608, 0.318, 1], [0.556, 0.215, 1],
              [0.403, 0.237, 1], [0.481, 0.149, 1], [0.437, 0.211, 1]], index=range(1, 9), columns=['密度', '含糖率', '好瓜'])
    negative_data = pd.DataFrame(
        data=[[0.666, 0.091, 0], [0.243, 0.267, 0], [0.245, 0.057, 0], [0.343, 0.099, 0], [0.639, 0.161, 0],
              [0.657, 0.198, 0],
              [0.360, 0.370, 0], [0.593, 0.042, 0], [0.719, 0.103, 0]], index=range(1, 10), columns=['密度', '含糖率', '好瓜'])
    # 数据集划分
    # p_n比例,进行数据集划分要保证划分后的正反例比例一致
    rate = np.ceil(positive_data.shape[0] / negative_data.shape[0])

    # 2.归一化
    std_positive_data, std_negative_data = normalization(positive_data, negative_data)

    # 一次验证有一个模型，最终得到八个模型，进行投票，票多为预测结果
    # 3.进行八折交叉验证std_positive_data.shape[0]+1
    error_rate_list = []
    for i in range(1, std_positive_data.shape[0] + 1):
        # 1.获取训练集
        data1 = std_positive_data[std_positive_data.index != i]
        data2 = std_negative_data[std_negative_data.index != i]
        train_data = pd.concat([data1, data2], join='inner', axis=0)
        train_data.reset_index(drop=True, inplace=True)
        x_train = train_data.iloc[:, :-1].values
        y_train = train_data[train_data.columns[-1]].values
        # 样本个数和特征值个数
        m_train = x_train.shape[0]
        d_train = x_train.shape[1]

        # 2.获取测试集
        test_data = pd.concat([std_positive_data[std_positive_data.index == i],
                               std_negative_data[std_negative_data.index == i]], join='inner', axis=0)
        test_data.reset_index(drop=True, inplace=True)
        x_test = test_data.iloc[:, :-1].values
        y_test = test_data[test_data.columns[-1]].values
        # 测试集样本个数
        m_test = x_test.shape[0]
        # print(train_data, '\n=================\n', test_data)

        # 3.求解模型参数
        beta = gradient_descend_method(m_train, d_train, x_train, y_train, alpha, iteration)

        # 5.预测和评估
        # 存放预测值列表
        y_predict = []
        one_error = 0
        # k遍历所以的测试集样本
        for k in range(0, m_test):
            # 特征值的列向量
            x_sample = x_test[k].T
            label = model(x_sample, beta)
            y_predict.append(label)
            if label != y_test[k]:
                one_error = (one_error + 1) / m_test
         # 第i次交叉验证的错误率
        error_rate_list.append(one_error)
        print("第%d次交叉验证的预测值为：" % i, y_predict)
        print("第%d次交叉验证的真实值为：" % i, y_test)
        # 评估--错误率
    mean_error_rate = np.mean(error_rate_list)
    print(mean_error_rate)
    # 2.进行投票，票多为预测结果
