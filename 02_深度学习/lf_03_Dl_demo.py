# 激活函数
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# 1.sigmoid激活函数--用在二分类的输出层
x = np.linspace(-10, 10, 1000)
y = tf.nn.sigmoid(x)
plt.plot(x, y)
plt.grid()
# 2.tanh激活函数
y1 = tf.nn.tanh(x)
plt.plot(x,y1)
plt.grid()
# 3.relu激活函数（用地比较多）
y2 = tf.nn.relu(x)
plt.plot(x,y2)
plt.grid()
# 4.leak_relu激活函数（对relu的改进）
y3 = tf.nn.leaky_relu(x)
plt.plot(x,y3)
plt.grid()
# 5.softmax激活函数--用在多分类问题的输出层（求类别可能的概率）
x = tf.constant([0.2, 0.02, 0.15, 1.3, 0.5, 0.06, 1.1, 0.05, 3.75])
y4 = tf.nn.softmax(x)
print(y4)