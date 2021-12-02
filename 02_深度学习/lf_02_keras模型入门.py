# 绘图
import seaborn as sns
# 数值计算
import numpy as np
import pandas as pd
# 机器学习——sklearn中的相关工具
# 加载数据
from sklearn.datasets import load_iris
# 划分训练集和测试集
from sklearn.model_selection import train_test_split
# 逻辑回归
from sklearn.linear_model import LogisticRegressionCV
# 深度学习——tf.keras中使用的相关工具
# 用于模型搭建
from tensorflow.keras.models import Sequential
# 构建模型的层和激活方法
from tensorflow.keras.layers import Dense, Activation
# 数据处理的辅助工具
from tensorflow.keras import utils

# 进行热编码
def one_hot_encode_object_array(arr):
    # 去重获取全部的类别以及索引值
    uniques, ids = np.unique(arr, return_inverse=True)
    # 返回热编码的结果
    return utils.to_categorical(ids, len(uniques))
# 1.获取数据
iris = load_iris()
col = iris.feature_names
iris_df = pd.DataFrame(iris.data, columns = col)
iris_df["species"] = iris.target
# sns.pairplot(iris_df,hue="species")
# 获取特征值和目标值
x = iris_df.iloc[:, :4]
y = iris_df.iloc[:, 4:]
# 2.数据基本处理
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=22)
# print("数据划分后训练集的大小：", x_train.shape)
# # 3.机器学习-逻辑回归
# estimator = LogisticRegressionCV()
# estimator.fit(x_train, y_train)
# print("机器学习的准确率为：", estimator.score(x_test, y_test))
# 4.keras深度学习
# 4.1数据处理
# 对训练集和测试集目标值进行热编码
y_train_ohe = one_hot_encode_object_array(y_train)
y_test_ohe = one_hot_encode_object_array(y_test)
# print("对目标值进行热编码后的结果：", y_train_ohe)
# 4.2模型构建--sequential
# 构建模型
model = Sequential([
    # 隐藏层
    Dense(10, activation="relu", input_shape=(4,)),
    # 隐藏层
    Dense(10, activation="relu"),
    # 输出层
    Dense(3, activation="softmax")
])
# 模型属性
print(model.summary())
# 绘制模型
# utils.plot_model(model, show_shapes=True)
# 4.3模型训练与评估
# 4.3.1模型编译
# 设置模型的相关参数：优化器，损失函数和评价指标
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])
# 4.3.2模型的训练:epochs,训练样本送入到网络中的次数，batch_size:每次训练的送入到网络中的样本个数
model.fit(x_train, y_train_ohe, batch_size=1, epochs=10, verbose=1)
# 4.3.3模型评估
# 返回的是损失函数和在compile模型时要求的指标
loss, accuracy = model.evaluate(x_test, y_test_ohe, verbose=1)
print("损失值为：", loss)
print("模型的准确率 = {:.2f}".format(accuracy))