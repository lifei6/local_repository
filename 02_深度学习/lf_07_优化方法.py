# 1.梯度下降法
import tensorflow as tf
from tensorflow.keras.optimizers import SGD
# # 1.1 实例化优化方法：SGD
# opt = SGD(learning_rate=0.1)
# # 1.2 定义要调的参数
# var = tf.Variable(1.0)
# # 1.3 定义损失函数：无参但有放回值
# loss = lambda: (var**2)/2.0
# # 1.4 计算梯度并对参数进行更新，步长为学习率*梯度
# opt.minimize(loss,[var]).numpy()
# # 1.5 输出参数更新结果
# print(var.numpy())
# 2.梯度下降算法的优化算法
# 2.1 momentum--动量梯度下降算法(这个参数表示之前的参数（w1,w2,...wi-1）所占权重)--对梯度进行调整
# 实例化一个优化器
# 另一种加快响应的算法（增大步长）是设置nesterov为Ture
opt = SGD(learning_rate=0.1, momentum=0.9
          # ,nesterov=True
        )
# 定义初始权重变量
var = tf.Variable(1.0)
var1 = var.value()
print(var1)
# 定义损失函数计算方法
loss = lambda : (var**2)/2.0
# 计算损失函数并更新权重变量：因为加入了momentum步长会增加
# 第一次更新
opt.minimize(loss, [var])
var2 = var.value()
print(var2)
# 第二次更新
opt.minimize(loss, [var])
var3 = var.value()
print(var3)
# 显示权重更新结果
print("第一次更新后步长为：{}".format(var1-var2))
print("第二次更新后步长为：{}".format(var2-var3))
# # 2.2.adagrad--调整迭代的学习率--对学习率进行调整
# # 实例化一个优化器
# from tensorflow.keras.optimizers import Adagrad
# opt = Adagrad(learning_rate=0.01, initial_accumulator_value=0.1, epsilon=1e-6)
# # 定义初始权重变量
# var = tf.Variable(1.0)
# var1 = var.value()
# print(var1)
# # 定义损失函数计算方法
# loss = lambda : (var**2)/2.0
# # 计算损失函数并更新权重变量：步长会减少
# # 第一次更新
# opt.minimize(loss, [var])
# var2 = var.value()
# print(var2)
# # 第二次更新
# opt.minimize(loss, [var])
# var3 = var.value()
# print(var3)
# # 显示权重更新结果
# print("第一次更新后步长为：{}".format(var1-var2))
# print("第二次更新后步长为：{}".format(var2-var3))
# 2.3 RMSprop算法--对学习率进行调整
# 实例化一个优化器
from tensorflow.keras.optimizers import RMSprop
opt = RMSprop(learning_rate=0.1, rho=0.9, epsilon=1e-6,centered=False)
# 定义初始权重变量
var = tf.Variable(1.0)
var1 = var.value()
print(var1)
# 定义损失函数计算方法
loss = lambda : (var**2)/2.0
# 计算损失函数并更新权重变量：
# 第一次更新
opt.minimize(loss, [var])
var2 = var.value()
print(var2)
# 第二次更新
opt.minimize(loss, [var])
var3 = var.value()
print(var3)
# 显示权重更新结果
print("第一次更新后步长为：{}".format(var1-var2))
print("第二次更新后步长为：{}".format(var2-var3))
# 2.4 Adam算法--对梯度和学习率都进行修正
# 实例化一个优化器
from tensorflow.keras.optimizers import Adam
opt = Adam(learning_rate=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
# 定义初始权重变量
var = tf.Variable(1.0)
var1 = var.value()
print(var1)
# 定义损失函数计算方法
loss = lambda : (var**2)/2.0
# 计算损失函数并更新权重变量：
# 第一次更新
opt.minimize(loss, [var])
var2 = var.value()
print(var2)
# 第二次更新
opt.minimize(loss, [var])
var3 = var.value()
print(var3)
# 显示权重更新结果
print("第一次更新后步长为：{}".format(var1-var2))
print("第二次更新后步长为：{}".format(var2-var3))