import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import metrics
import time
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

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
    dataset = pd.concat([positive_data, negative_data],join='inner',axis=0)
    dataset.reset_index(drop=True,inplace=True)
    x = dataset[['密度','含糖率']]
    y = dataset['好瓜']
    # print(x,y)
    # 2.分割训练集和测试集
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=22)

    # 3.实例化模型对象并进行训练
    LDA_model = LinearDiscriminantAnalysis()
    LDA_model.fit(x_train,y_train)

    # 4.预测与评估
    y_predict = LDA_model.predict(x_test)

    print('混淆矩阵','\n',metrics.confusion_matrix(y_test,y_predict))
    print(metrics.classification_report(y_test,y_predict,target_names=['坏瓜','好瓜']))
    print(LDA_model.coef_)

    # 绘图
    good_melon = dataset[dataset['好瓜'] == 1]
    bad_melon = dataset[dataset['好瓜'] == 0]
    # print(good_melon,bad_melon)
    plt.scatter(bad_melon['密度'], bad_melon['含糖率'], marker='o', color='r', s=100, label='坏瓜')
    plt.scatter(good_melon['密度'], good_melon['含糖率'], marker='o', color='g', s=100, label='好瓜')
    # 下面绘制直线
    data = np.array(dataset.iloc[:,:-1].values)
    X0 = np.array(data[:8])
    X1 = np.array(data[8:])
    # 求正反例均值
    miu0 = np.mean(X0, axis=0).reshape((-1, 1))
    miu1 = np.mean(X1, axis=0).reshape((-1, 1))
    # 求协方差
    cov0 = np.cov(X0, rowvar=False)
    cov1 = np.cov(X1, rowvar=False)
    print(cov0)
    print(cov1)
    # 求出w
    S_w = np.mat(cov0 + cov1)
    print(S_w,S_w.I)
    Omiga = S_w.I * (miu0 - miu1)
    # 画出点、直线
    plt.scatter(X0[:, 0], X0[:, 1], c='b', label='+', marker='+')
    plt.scatter(X1[:, 0], X1[:, 1], c='m', label='-', marker='_')
    plt.plot([0, 1], [0, -Omiga[0] / Omiga[1]], label='y')
    plt.xlabel('密度', fontproperties='SimHei', fontsize=15, color='green');
    plt.ylabel('含糖率', fontproperties='SimHei', fontsize=15, color='green');
    plt.title(r'LinearDiscriminantAnalysis', fontproperties='SimHei', fontsize=25);
    plt.legend()
    plt.show()
