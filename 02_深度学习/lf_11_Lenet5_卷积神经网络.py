# 导入相应的包
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# 数据加载
from tensorflow.keras.datasets import mnist
# 模型搭建
from tensorflow.keras.models import Sequential
# 网络层
from tensorflow.keras.layers import Conv2D,MaxPool2D,Dense,Activation,Dropout,BatchNormalization,Flatten
# 辅助工具
from tensorflow.keras import utils

# 1.数据加载
(train_images,train_labels), (test_images,test_labels)=mnist.load_data()
# 2.数据处理
# 2.1维度调整NHWC
train_images = tf.reshape(train_images,(train_images.shape[0],train_images.shape[1],
                                        train_images.shape[2],1))
test_images = tf.reshape(test_images,(test_images.shape[0],test_images.shape[1],test_images.shape[2],1))
# 2.2目标值进行one-hot编码
n_classes = 10
train_labels_ohe = utils.to_categorical(train_labels,n_classes)
test_labels_ohe = utils.to_categorical(test_labels,n_classes)
# 3.网络搭建
# lenet-5 是两个卷积层加池化层，最后一个全连接层
# 构建一个序列模型
net = Sequential()
# 第一个卷积层：6个5*5的卷积核，激活函数为sigmoid,输出24*24的数据
net.add(Conv2D(filters=6,kernel_size=(5,5),padding='valid',strides=1,activation='sigmoid',input_shape=(28,28,1)))
# net.add(BatchNormalization())
# net.add(Dropout(0.2))
# 添加池化层--最大池化（平均池化--AvgPool2D会使特征缓和一般编译）:池化大小为2*2，步长为2
# 输出12*12的数据
net.add(MaxPool2D(pool_size=(2,2),strides=2,padding='valid'))
# 第二个卷积层:16个5*5的卷积核，激活函数为sigmoid，输出8*8的数据
net.add(Conv2D(filters=16,kernel_size=(5,5),strides=1,padding='valid',activation='sigmoid'))
# 添加池化层
# 输出4*4的数据
net.add(MaxPool2D(pool_size=(2,2),strides=2))
# 调整维度--全连接层是一维输入的
# 输出16*16位数据
net.add(Flatten())
# 第一个隐层：120个神经元,激活函数为sigmoid
net.add(Dense(120,activation='sigmoid',input_shape=(256,)))
net.add(BatchNormalization())
net.add(Dropout(0.2))
# 第二个隐层：84个神经元，激活函数为sigmoid
net.add(Dense(84))
net.add(BatchNormalization())
net.add(Activation('sigmoid'))
net.add(Dropout(0.2))
# 第三个输出层：10个神经元，激活函数为softmax
net.add(Dense(10,activation='softmax'))

# 4.模型的编译--损失函数，优化方法，评价标准
net.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# 5.模型训练
history = net.fit(train_images,train_labels_ohe,epochs=5,
                  validation_data=(test_images,test_labels_ohe),verbose=1)
print("打印损失函数和准确率", history.history)
# 6.模型评估
loss,accuracy = net.evaluate(test_images,test_labels_ohe,verbose=1)
print("测试集的准确率为：", accuracy)
# 7.模型保存与加载
# 保存
net.save('./Lenet-5_model.h5')
# 加载
model = tf.keras.models.load_model("./Lenet-5_model.h5")
model.summary()

