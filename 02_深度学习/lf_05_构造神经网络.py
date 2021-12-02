import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# 1.使用sequential构造简单的序列模型
model1 = keras.Sequential([
    # 第一层：3个神经元，激活函数为relu，初始化方法为he_normal，输入个数为3，偏置为0
    layers.Dense(3, activation="relu", use_bias=True, kernel_initializer="he_normal",
                 bias_initializer="zeros", input_shape=(3,), name="layer1"),
    # 第二层：2个神经元，激活函数为relu，初始化方法为he_normal
    layers.Dense(2, activation="relu", kernel_initializer="he_normal", name='layer2'),
    # 第三层：2个神经元(两个输出为二分类问题)，激活函数为sigmoid，初始化方法为he_normal
    layers.Dense(2, activation="sigmoid", kernel_initializer='he_normal',name='layer3')
],name='my_Sequential')
model1.summary()
# 2.利用function api进行构建
# 定义模型的输入
inputs = tf.keras.Input(shape=(3,), name="input")
# 第一层：3个神经元，激活函数为relu，初始化方法为he_normal
x = tf.keras.layers.Dense(3, activation="relu", kernel_initializer="he_normal", name="layer1")(inputs)
# 第二层：2个神经元，激活函数为relu，初始化方法为he_normal
x = tf.keras.layers.Dense(2, activation="relu", kernel_initializer="he_normal", name='layer2')(x)
# 第三层（输出层）：2个神经元(两个输出为二分类问题)，激活函数为sigmoid，初始化方法为he_normal
outputs = tf.keras.layers.Dense(2, activation="sigmoid", kernel_initializer="he_normal", name='layer3')(x)
model2 = tf.keras.Model(inputs,outputs,name="Function API Model")
model2.summary()
# 3.通过model的子类来构建模型
# 构建一个模型子类
class MyModel(tf.keras.Model):
    # 在init方法中定义网络的层结构
    def __init__(self):
        super(MyModel, self).__init__()
        # 第一层：3个神经元，激活函数为relu，初始化方法为he_normal，输入个数为3，偏置为0
        self.layer1 = layers.Dense(3, activation="relu", use_bias=True, kernel_initializer="he_normal",
                                    bias_initializer="zeros", input_shape=(3,), name="layer1")
        # 第二层：2个神经元，激活函数为relu，初始化方法为he_normal
        self.layer2 = layers.Dense(2, activation="relu", kernel_initializer="he_normal", name='layer2')
        # 第三层：2个神经元(两个输出为二分类问题)，激活函数为sigmoid，初始化方法为he_normal
        self.layer3 = layers.Dense(2, activation="sigmoid", kernel_initializer="he_normal",name='layer3')
    # 在call方法中完成前向传播
    def call(self, inputs):
        x = self.layer1(inputs)
        x = self.layer2(x)
        return self.layer3(x)
# 实例化一个模型
model = MyModel()
# 设置一个输入调用模型（否则无法使用summary）
x = tf.ones((1,3))
y = model(x)
model.summary()