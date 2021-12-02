import tensorflow as tf
import numpy as np
# # 1.创建张量
# # 1.1创建int32类型的0维张量，即标量
# rank_0_tensor = tf.constant(4)
# print(rank_0_tensor)
# # 1.2创建float32类型的1维张量（vector）
# rank_1_tensor = tf.constant([1.2, 1.1, 3.5])
# print(rank_1_tensor)
# # 1.3创建float64类型的2维张量（matrix）
# rank_2_tensor = tf.constant([[1.1, 1.3, 1.4], [2.1, 2.2, 2.3]], dtype=np.float64)
# print(rank_2_tensor)
# # 2.tensor转ndarray
# # 2.1
# array = np.array(rank_2_tensor)
# print(array)
# # 2.2
# print(rank_2_tensor.numpy())
# # 3.常用函数
# # 3.1数学运算
# a = tf.constant([[1, 2], [3, 4]])
# b = tf.constant([[2, 3], [10, 5]])
# print("加法运算结果：", tf.add(a, b))
# print("乘法运算结果：", tf.multiply(a, b))
# print("矩阵乘法运算：", tf.matmul(a, b))
# # 3.2聚合运算
# print("张量中的最大值：", tf.reduce_max(a))
# print("张量中的最小值：", tf.reduce_min(a))
# print("张量求和：", tf.reduce_sum(a))
# print("张量平均值：", tf.reduce_mean(a))
# print("张量最大值索引：", tf.argmax(b))
# print("张量最小值索引：", tf.argmin(b))
# 4.定义变量
my_variable = tf.Variable([[1, 2], [3, 4]])
print("变量的维度：", my_variable.shape)
print("变量的类型：", my_variable.dtype)
print("变量的numpy数值：", my_variable.numpy())
# 修改变量--形状必须一样
print("修改后的变量：", my_variable.assign([[1, 1], [2, 2]]))