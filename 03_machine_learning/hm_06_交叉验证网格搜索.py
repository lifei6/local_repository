from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
# 1.获取数据
iris = load_iris()
# 2.划分数据集
# x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集目标值、测试集目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
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
estimator = KNeighborsClassifier()
# 4.2 模型选择与调优--进行交叉验证和网格搜索
# 准备要调的超参数（以字典的形式传输）
param_dict = {"n_neighbors": [1, 3, 5, 7]}
# 分类问题的交叉验证，网格搜索
estimator = GridSearchCV(estimator, param_dict, cv=4)
# 4.3 调用fit方法进行训练
estimator.fit(x_train, y_train)
# 5.模型评估
# 5.1 比对真实值和预测值
ret = estimator.predict(x_test)
print(ret == y_test)
# 5.2 直接计算准确率
score = estimator.score(x_test, y_test)
print("准确率为：\n", score)
# 5.3 查看交叉验证，网格搜索的一些属性
print("在交叉验证中验证的最好结果：\n", estimator.best_score_)
print("最好的参数模型：\n", estimator.best_estimator_)
print("每次交叉验证后的准确率结果：\n", estimator.cv_results_)