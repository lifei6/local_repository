# sklearn.neighbors.KNeighborsClassifier(n_neighbors=5,algorithm='auto')
# n_neighbors：int,可选（默认= 5），k_neighbors查询默认使用的邻居数
# algorithm：{‘auto’，‘ball_tree’，‘kd_tree’，‘brute’}
# 导入最近邻算法KNN
from sklearn.neighbors import KNeighborsClassifier
# 1.构造一组数据
x = [[0], [1], [10], [20]]
y = [1, 1, 2, 2]
# 2.训练模型
# 2.1 实例化一个估计器类
estimator = KNeighborsClassifier(n_neighbors=1)
# 2.2 调用fit()方法进行训练模型
estimator.fit(x, y)
# 3.数据预测
ret1 = estimator.predict([[2]])
print(ret1)
ret2 = estimator.predict([[13]])
print(ret2)



