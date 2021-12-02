# 1.获取数据集
# 2.数据基本处理
# 3.特征工程
# 4.机器学习(模型训练)
# 5.模型评估

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
# 1.获取数据
iris = load_iris()
# 2.划分数据集
# x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集目标值、测试集目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)
print(y_test)
# 3.特征工程--特征预处理
# 标准化处理
# 3.1 实列化一个转化器类
transfer = StandardScaler()
# 3.2 调用fit_transform()进行转换,fit就是计算平均值和方差
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# print("标准化处理后的数据：/n", data)
# 4.采用KNN算法训练模型
# 4.1 实例化一个估计器类
estimator = KNeighborsClassifier(n_neighbors=9, algorithm='auto')
# 4.2 调用fit方法进行训练
estimator.fit(x_train, y_train)
# 5.模型评估
# 5.1 比对真实值和预测值
ret = estimator.predict(x_test)
print(ret == y_test)
# # 判断预测的准确性
# predict_list = []
# for i in range(y_test.shape[0]):
#     if y_test[i] == ret[i]:
#         predict_list.append("True")
#     else:
#         predict_list.append("False")
#
# print(predict_list)
# 5.2 直接计算准确率
score = estimator.score(x_test, y_test)
print("准确率为：\n", score)

