# 1.L1，L2正则化
# 2.Dropout（失活层）--对这层层进行一定概率的神经元失活
import tensorflow as tf
from tensorflow.keras.layers import Dropout
import numpy as np
# 2.1 构造失活层
# rate为失活概率
layer = Dropout(rate=0.2, input_shape=(2,))
# 2.2 构造五个样本的数据
data = np.arange(1,11).reshape((5,2)).astype(np.float32)
print(data)
# 2.3 将数据送入dropout层进行训练,training=False时该层不起作用
outputs = layer(data, training=True)
print(outputs)
# 3.EarlyStopping--提前停止正则化
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import SGD
# 定义回调函数
# 当连续3个epoch,loss不下降则停止训练
# patience指loss不在下降后执行训练的次数
callback = EarlyStopping(monitor='loss',patience=3)
# 构造一个一层的网络
model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
# 对神经网络进行配置--模型的编译
# 设置损失函数和梯度下降法
# 实例化一个优化方法
opt = SGD()
model.compile(optimizer=opt, loss='mse')
# 模型训练
history = model.fit(np.arange(100).reshape(5,20),np.array([0,1,2,1,2]),
                    epochs=10,batch_size=1,callbacks=[callback],verbose=1)
# 打印运行epoch
len(history.history['loss'])
# 4.BN层(批标准化层)--先进行标准化在进行重构（包括尺度变化和平移）--BatchNormalization
# 直接将其放入神经网络中的结构中即可
# api: tf.keras.layers.BatchNormalization(epsilon=0.001,center=True,scale=True,
# beta_initializer='zeros',gamma_initializer='ones')