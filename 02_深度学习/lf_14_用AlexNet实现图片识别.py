import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Activation,Dropout,BatchNormalization,Dense
from tensorflow.keras import utils
# 1.数据的加载
(x_train,y_train), (x_test,y_test) = mnist.load_data()
# 2.数据处理
# 2.1调整数据维度NHWC
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],x_train.shape[2],1))
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],x_test.shape[2],1))
# 2.1数据的随机获取
# 对获取的样本图片（28，28，1）进行填充
# AlexNet 输入为（n,227,227,1）
def get_train(num):
    """
    随机获取训练集数目,并且进行填充
    :param num:
    :return:
    """
    index = np.random.randint(0,x_train.shape[0],num)
    get_x_train = tf.image.resize_with_pad(x_train[index],227,227)
    get_y_train = y_train[index]
    return get_x_train.numpy(), get_y_train

def get_test(num):
    """
    随机获取测试集数目，并且进行填充
    :param num:
    :return:
    """
    index = np.random.randint(0,x_test.shape[0],num)
    get_x_test = tf.image.resize_with_pad(x_test[index],227,227)
    get_y_test = y_test[index]
    return get_x_test.numpy(), get_y_test

(x_train, y_train) = get_train(20)
(x_test, y_test) = get_test(2)

# 2.3对目标值进行one-hot编码
n_classes = 10
y_train = utils.to_categorical(y_train,n_classes)
y_test = utils.to_categorical(y_test,n_classes)
# 3.AlexNet模型
model = Sequential([
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
# 4.模型的编译
model.compile(loss = 'categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# 5.训练
history = model.fit(x_train,y_train,epochs=5,batch_size=2,verbose=1,validation_split=0.1)
print(history.history)
# 6.评估
loss, accuracy = model.evaluate(x_test,y_test,verbose=1)
print("准确率为：", accuracy)

