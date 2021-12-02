import tensorflow as tf
import tensorflow.keras
# Xevizer初始化
# 1.Xavizer（glorot）正太分布初始化--随机初始化
# 1.1实例化一个初始化器
initializer1 = tf.keras.initializers.glorot_normal()
# 1.2生成指定规模的权重参数
values1 = initializer1((9,1))
print(values1)
# 2.Xavizer均匀分布初始化--标准初始化
initializer2 = tf.keras.initializers.glorot_uniform()
values2 = initializer2((9,1))
print(values2)
# he初始化
# 1.正态分布he初始化
initializer3 = tf.keras.initializers.he_normal()
values3 = initializer3((9,1))
print(values3)
# 2.均匀分布he初始化
initializer4 = tf.keras.initializers.he_uniform()
values4 = initializer4((9,1))
print(values4)
