# 分类任务
# 1.多分类问题中的交叉熵损失（CategorialCrossentyopy）--使用softmax激活
import tensorflow as tf
from tensorflow.keras.losses import CategoricalCrossentropy
# 构造真实值与预测值--真实值为one-hot编码，预测值输出为概率
y_ture = tf.constant([[0,1,0],[0,0,1]])
y_pre = tf.constant([[0.05,0.95,0],[0.1,0.1,0.8]])
# 实例化交叉熵损失
cce = CategoricalCrossentropy()
# 计算损失结果
print("多分类问题损失结果为：",cce(y_ture,y_pre).numpy())
# 2.二分类问题中的交叉熵损失函数
from tensorflow.keras.losses import BinaryCrossentropy
y_ture = tf.constant([[0],[1]])
y_pre = tf.constant([[0.4],[0.6]])
bce = BinaryCrossentropy()
print("二分类问题损失结果为：", bce(y_ture,y_pre).numpy())



# 回归问题
# 1.MAE损失（MeanAbsoluteError）(L1 loss)
from tensorflow.keras.losses import MeanAbsoluteError
y_ture = tf.constant([[0.],[1.]])
y_pre = tf.constant([[0.],[1.]])
mae = MeanAbsoluteError()
print("回归问题mae损结果为：", mae(y_ture,y_pre).numpy())
# 2.MSE损失（MeanSquareError）(L2 loss)
from tensorflow.keras.losses import MeanSquaredError
y_ture = tf.constant([[0.],[1.]])
y_pre = tf.constant([[0.],[1.]])
mse = MeanSquaredError()
print("回归问题mse损结果为：", mse(y_ture,y_pre).numpy())
# 3.smooth l1损失(Huber)
from tensorflow.keras.losses import Huber
y_ture = tf.constant([[0.],[1.]])
y_pre = tf.constant([[0.01],[1.1]])
h = Huber()
print("smooth l1损失结果：", h(y_ture, y_pre).numpy())