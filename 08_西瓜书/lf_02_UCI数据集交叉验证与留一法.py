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
from lf_01_sigmoid模型 import normalization, gradient_descend_method, model

# 设置学习率
alpha = 0.05
# 设置迭代次数
iteration = 1000
# 设置交叉验证的次数
N = 10

# 1.txt文件没有特征名的读取处理情况
# header表示是否读取表头为列索引
data1 = pd.read_csv('./data_sets/iris.txt', header=None)
common_columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
data1.columns = common_columns

# print(data1.head(5))

# 2.进行数据集划分以及正反例划分
# 判断是否存在缺失值
print('不存在缺失值：', np.all(pd.notnull(data1)))
# Iris-setosa类1
# Iris-versicolor类2
# Iris-virginica类3
# ECOC编码--类编码
c1 = [1, 0, 0, 0, 1, 1]
c2 = [0, 1, 0, 1, 0, 1]
c3 = [0, 0, 1, 1, 1, 0]

# 6个分类器模型参数存放矩阵(d+1)*f
beta_matrix = np.zeros((5, 6))

# 创建一个用于接收DataFrame变量的变量
p_data_1 = pd.DataFrame()
n_data_1 = pd.DataFrame()
for f in range(1, 7):
    # 需要训练6个二分类器
    # 分类器正反例设置
    if f == 1:
        p_data_1 = data1[data1['class'] == 'Iris-setosa']
        p_data_1.loc[p_data_1.index, 'class'] = 1
        p_data_1.reset_index(drop=True, inplace=True)
        n_data_1 = data1[data1['class'] != 'Iris-setosa']
        n_data_1.loc[n_data_1.index, 'class'] = 0
        n_data_1.reset_index(drop=True, inplace=True)
        print('%d我执行了' % f)
    elif f == 2:
        p_data_1 = data1[data1['class'] == 'Iris-versicolor']
        p_data_1.loc[p_data_1.index, 'class'] = 1
        p_data_1.reset_index(drop=True, inplace=True)
        n_data_1 = data1[data1['class'] != 'Iris-versicolor']
        n_data_1.loc[n_data_1.index, 'class'] = 0
        n_data_1.reset_index(drop=True, inplace=True)
        print('%d我执行了' % f)
    elif f == 3:
        p_data_1 = data1[data1['class'] == 'Iris-virginica']
        p_data_1.loc[p_data_1.index, 'class'] = 1
        p_data_1.reset_index(drop=True, inplace=True)
        n_data_1 = data1[data1['class'] != 'Iris-virginica']
        n_data_1.loc[n_data_1.index, 'class'] = 0
        n_data_1.reset_index(drop=True, inplace=True)
        print('%d我执行了' % f)
    elif f == 4:
        # 正反例互换
        n_data_1 = data1[data1['class'] == 'Iris-setosa']
        n_data_1.loc[n_data_1.index, 'class'] = 0
        n_data_1.reset_index(drop=True, inplace=True)
        p_data_1 = data1[data1['class'] != 'Iris-setosa']
        p_data_1.loc[p_data_1.index, 'class'] = 1
        p_data_1.reset_index(drop=True, inplace=True)
        print('%d我执行了' % f)
    elif f == 5:
        n_data_1 = data1[data1['class'] == 'Iris-versicolor']
        n_data_1.loc[n_data_1.index, 'class'] = 0
        n_data_1.reset_index(drop=True, inplace=True)
        p_data_1 = data1[data1['class'] != 'Iris-versicolor']
        p_data_1.loc[p_data_1.index, 'class'] = 1
        p_data_1.reset_index(drop=True, inplace=True)
        print('%d我执行了' % f)
    elif f == 6:
        n_data_1 = data1[data1['class'] == 'Iris-virginica']
        n_data_1.loc[n_data_1.index, 'class'] = 0
        n_data_1.reset_index(drop=True, inplace=True)
        p_data_1 = data1[data1['class'] != 'Iris-virginica']
        p_data_1.loc[p_data_1.index, 'class'] = 1
        p_data_1.reset_index(drop=True, inplace=True)
        print('%d我执行了' % f)
    # 正反例比例
    # print("正反例比例n_p为：", np.ceil(n_data_1.shape[0], p_data_1.shape[0]))
    # 调用归一化函数
    std_p_1, std_n_1 = normalization(p_data_1, n_data_1)
    # 3. 10折交叉验证法--只为进行模型的评估，不是最终模型，最终模型由全部数据送入训练得出
    step = 10
    error_rate_list = []
    for i in range(0, N):
        # 3.1获取每次交叉验证的测试集和训练集
        test_data = pd.concat([std_p_1.iloc[i::step, :], std_n_1.iloc[i::step, :]],
                              join='inner', axis=0)
        test_data.reset_index(drop=True, inplace=True)
        # 删除满足条件的行 --操作
        train_data = pd.concat([std_p_1.drop(std_p_1.index[i::step]), std_n_1.drop(std_n_1.index[i::step])],
                               join='inner', axis=0)
        train_data.reset_index(drop=True, inplace=True)
        # print(test_data.shape)
        x_test = test_data.iloc[:, :-1].values
        y_test = test_data[test_data.columns[-1]].values
        x_train = train_data.iloc[:, :-1].values
        y_train = train_data[train_data.columns[-1]].values

        # 样本个数
        m_train = x_train.shape[0]
        m_test = x_test.shape[0]
        # 特征值个数
        d_train = x_train.shape[1]

        # 3.2求解模型参数
        beta = gradient_descend_method(m_train, d_train, x_train, y_train, alpha, iteration)

        # 3.3预测和评估
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
        # print("第%d次交叉验证的预测值为：" % i, y_predict)
        # print("第%d次交叉验证的真实值为：" % i, y_test)
    # 4.f1分类器平均错误率
    mean_error_rate = np.mean(error_rate_list)*100
    print("%d分类器%d次交叉验证的平均错误率为：%.2f%%" % (f, N, mean_error_rate))

    # 4.全部数据送入训练得到最终的模型
    all_data = pd.concat([std_p_1, std_n_1], join='inner', axis=0)
    all_data.reset_index(drop=True, inplace=True)
    # 训练集特征值和目标值
    x_train_all = all_data.iloc[:, :-1].values
    y_train_all = all_data[all_data.columns[-1]].values
    m = x_train_all.shape[0]
    d = x_train_all.shape[1]
    # 最终的beta值
    new_beta = gradient_descend_method(m, d, x_train_all, y_train_all, alpha, iteration)
    beta_matrix[:, f-1] = new_beta
    # 最终模型
    # 4.模型构造z = w.T*x +b作为sigmoid函数的自变量
    y_label = []
    error = 0
    # k遍历所以的测试集样本
    for k in range(0, m):
        # 特征值的列向量
        x_sample = x_train_all[k].T
        label = model(x_sample, new_beta)
        y_label.append(label)
        if label != y_train_all[k]:
            error = (error + 1) / m
    print("预测值为：", y_label)
    print("真实值为：", y_train_all)
    # 评估--错误率
    print("错误率", error)

# 6个模型的参数
print('模型参数矩阵', '\n', beta_matrix)
