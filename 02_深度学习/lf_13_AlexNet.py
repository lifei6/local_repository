import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Activation,Dropout,BatchNormalization,Dense

# 1.模型构造
AlexNet = Sequential([
    # 卷积层：96个核，大小为11*11，步长为4
    Conv2D(filters=96,kernel_size=(11,11),strides=4,activation='relu',input_shape=(227,227,1)),
    # 池化层：窗口大小3*3，步长为2
    MaxPool2D(pool_size=(3,3),strides=2),
    # 卷积层：256个核，大小为5*5，步长为1，填充到与输入大小一致
    Conv2D(filters=256,kernel_size=(5,5),strides=1,padding='same',activation='relu'),
    # 池化层：窗口大小为3*3，步长为2
    MaxPool2D(pool_size=(3,3),strides=2),
    # 卷积层：384个核，大小为3*3，步长为1，填充到与输入大小一致
    Conv2D(filters=384,kernel_size=(3,3),strides=1,padding='same',activation='relu'),
    # 卷积层：384个核，大小为3*3，步长为1，填充到与输入大小一致
    Conv2D(filters=384,kernel_size=(3,3),strides=1,padding='same',activation='relu'),
    # 卷积层：256个核，大小为3*3，步长为1，填充到与输入大小一致
    Conv2D(filters=256,kernel_size=(3,3),strides=1,padding='same',activation='relu'),
    # 伸展为一维向量
    tf.keras.layers.Flatten(),
    # 全连接层：4096个神经元，激活函数为relu
    Dense(4096,activation='relu'),
    # 随机失活
    Dropout(0.5),
    # 全连接层：4096个神经元，激活函数为relu
    Dense(4096,activation='relu'),
    # 随机失活
    Dropout(0.5),
    # 输出层：10个神经元，激活函数为softmax
    Dense(10,activation='softmax')
])
# 2.构造输入数据，查看模型网络
x = tf.random.uniform((1,227,227,1))
y = AlexNet(x)
AlexNet.summary()
# 3.模型保存
AlexNet.save('./AlexNet.h5')
