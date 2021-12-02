import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, classification_report, roc_auc_score

# 1.获取数据
names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                  names=names)
print(data.head())
# 2.基本数据处理
# 2.1 删除缺失值
# 2.1.1 缺失值替换
# 判断是否有缺失值
# print("缺失值存在吗？", np.all(pd.notnull(data)))
data = data.replace(to_replace="?", value=np.nan)
# 2.1.2 删除缺失值
data = data.dropna()
# 2.2 找到特征值和目标值
x = data.iloc[:, 1:10]
y = data['Class']
# 2.3 进行数据划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)
# 3.特征预处理
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 4.特征工程--逻辑回归
estimator = LogisticRegression()
estimator.fit(x_train, y_train)
# 5.模型评估
# 5.1 真实值与预测值的比较，以及模型得分
y_predict = estimator.predict(x_test)
print("预测值与真实值的比较：\n", y_predict == y_test)
score = estimator.score(x_test, y_test)
print(score)
# 5.2 分类评估报告--精确性（precision），召回率(recall)，f1-score(衡量模型的稳定性)，准确性（accuracy）
ret = classification_report(y_test, y_predict, labels=[2, 4], target_names=['良性', '恶性'])
print(ret)
# 5.3 对于样本不均衡得二分类问题，记得用roc曲线auc指标去评估一下，越接近于1越好
# 真实值(y_test)的标记必须为0，1,预测值没有要求
# 将目标值标志进行转换
y_test = np.where(y_test > 3, 1, 0)
print("auc指标：\n", roc_auc_score(y_test, y_predict))