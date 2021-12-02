# x 数据集的特征值
# y 数据集的标签值
# test_size 测试集的大小，一般为float
# random_state 随机数种子,不同的种子会造成不同的随机采样结果。相同的种子采样结果相同。
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# 1.获取数据
iris = load_iris()
print(iris.feature_names)
# 2.进行数据划分
# 训练集的特征值x_train 测试集的特征值x_test 训练集的目标值y_train 测试集的目标值y_test
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
print("x_train:\n", x_train.shape)
# 随机数种子
x_train1, x_test1, y_train1, y_test1 = train_test_split(iris.data, iris.target, random_state=6)
x_train2, x_test2, y_train2, y_test2 = train_test_split(iris.data, iris.target, random_state=6)
print("如果随机数种子不一致：\n", x_train == x_train1)
print("如果随机数种子一致：\n", x_train1 == x_train2)
