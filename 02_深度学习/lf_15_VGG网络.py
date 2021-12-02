import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Activation,Dropout,BatchNormalization,Dense
from tensorflow.keras import utils


# 1.定义一个vgg块
def vgg_block(num_conv2d,num_filters):
    # 构造一个序列模型
    vgg_blk = Sequential()
    # 添加卷积层
    for _ in range(num_conv2d):
        vgg_blk.add(Conv2D(filters=num_filters,kernel_size=3,padding='same',activation='relu'))
    # 添加池化层
    vgg_blk.add(MaxPool2D(pool_size=2,strides=2))
    return vgg_blk


# 2.构造一个卷积层参数列表
conv_arch = ((2, 64), (2, 128), (3, 256), (3, 512), (3, 512))


# 3.搭建vgg网络
def vgg(conv_list):
    # 构建一个序列模型
    vgg = Sequential()
    # 添加卷积块
    for (num_conv2d, num_filters) in conv_list:
        vgg.add(vgg_block(num_conv2d, num_filters))
    # 添加全连接层
    vgg.add(Sequential([
        # 转化为一维向量
        tf.keras.layers.Flatten(),
        # 添加全连接层
        Dense(4096,activation='relu'),
        Dropout(0.5),
        Dense(4096, activation='relu'),
        Dropout(0.5),
        Dense(10,activation='softmax')
    ]))
    return vgg


# 4.实例化vgg
net = vgg(conv_arch)
# 5.构造输入数据，调用summary进行结构查看
x = tf.random.uniform((1,224,224,1))
y = net(x)
net.summary()