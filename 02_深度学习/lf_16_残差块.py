import tensorflow as tf
from tensorflow.keras import layers,activations
class Residual(tf.keras.Model):
    """残差块"""
    # 定义网络结构
    def __init__(self,num_channels,use_1x1conv=False,strides=1):
        super(Residual,self).__init__()
        # 卷积层
        self.conv1 = layers.Conv2D(num_channels,kernel_size=3,padding='same',strides=strides)
        # 卷积层
        self.conv2 = layers.Conv2D(num_channels,kernel_size=3,strides=strides)
        # 判断是否使用1x1的卷积层
        if use_1x1conv:
            self.conv3 = layers.Conv2D(num_channels,kernel_size=1,strides=strides)
        else:
            self.conv3 = None
        # bn层
        self.bn1 = layers.BatchNormalization()
        self.bn2 = layers.BatchNormalization()
    # 定义前向传播
    def call(self,x):
        y = activations.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(y))
        if self.conv3:
            x = self.conv3(x)
        outputs = activations.relu(y+x)
        return outputs