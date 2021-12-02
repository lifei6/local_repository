import tensorflow as tf
from tensorflow.keras import layers,activations
from tensorflow.keras.layers import Conv2D,MaxPool2D,Dense,BatchNormalization,Activation,GlobalAvgPool2D
# 1.搭建残差块
class Residual(tf.keras.Model):
    # 指明残差块的通道数，是否使用1*1卷积，步长
    def __init__(self, num_channels, use_1x1conv=False, strides=1):
        super(Residual, self).__init__()
        # 卷积层：指明卷积核个数，padding,卷积核大小，步长
        self.conv1 = layers.Conv2D(num_channels,
                                   padding='same',
                                   kernel_size=3,
                                   strides=strides)
        # 卷积层：指明卷积核个数，padding,卷积核大小，步长
        self.conv2 = layers.Conv2D(num_channels, kernel_size=3, padding='same')
        if use_1x1conv:
            self.conv3 = layers.Conv2D(num_channels,
                                       kernel_size=1,
                                       strides=strides)
        else:
            self.conv3 = None
        # 指明BN层
        self.bn1 = layers.BatchNormalization()
        self.bn2 = layers.BatchNormalization()

    # 定义前向传播过程
    def call(self, X):
        # 卷积，BN，激活
        Y = activations.relu(self.bn1(self.conv1(X)))
        # 卷积，BN
        Y = self.bn2(self.conv2(Y))
        # 对输入数据进行1*1卷积保证通道数相同
        if self.conv3:
            X = self.conv3(X)
        # 返回与输入相加后激活的结果
        return activations.relu(Y + X)
# 2.搭建残差模块
class ResnetBlock(tf.keras.layers.Layer):
    # 网络层的定义：输出通道数（卷积核个数），模块中包含的残差块个数，是否为第一个模块
    def __init__(self,num_channels, num_residuals, first_block=False):
        super(ResnetBlock, self).__init__()
        # 模块中的网络层
        self.listLayers=[]
        # 遍历模块中所有的层
        for i in range(num_residuals):
            # 若为第一个残差块并且不是第一个模块，则使用1*1卷积，步长为2（目的是减小特征图，并增大通道数）
            if i == 0 and not first_block:
                self.listLayers.append(Residual(num_channels, use_1x1conv=True, strides=2))
            # 否则不使用1*1卷积，步长为1
            else:
                self.listLayers.append(Residual(num_channels))
    # 定义前向传播过程
    def call(self, X):
        # 所有层依次向前传播即可
        for layer in self.listLayers.layers:
            X = layer(X)
        return X
# 3.搭建resnet
class ResNet(tf.keras.Model):
    # 初始化：指定每个模块中的残差快的个数
    def __init__(self,num_blocks):
        super(ResNet, self).__init__()
        # 输入层：7*7卷积，步长为2
        self.conv=layers.Conv2D(64, kernel_size=7, strides=2, padding='same')
        # BN层
        self.bn=layers.BatchNormalization()
        # 激活层
        self.relu=layers.Activation('relu')
        # 最大池化层
        self.mp=layers.MaxPool2D(pool_size=3, strides=2, padding='same')
        # 第一个block，通道数为64
        self.resnet_block1=ResnetBlock(64,num_blocks[0], first_block=True)
        # 第二个block，通道数为128
        self.resnet_block2=ResnetBlock(128,num_blocks[1])
        # 第三个block，通道数为256
        self.resnet_block3=ResnetBlock(256,num_blocks[2])
        # 第四个block，通道数为512
        self.resnet_block4=ResnetBlock(512,num_blocks[3])
        # 全局平均池化
        self.gap=layers.GlobalAvgPool2D()
        # 全连接层：分类
        self.fc=layers.Dense(units=10,activation=tf.keras.activations.softmax)
    # 前向传播过程
    def call(self, x):
        # 卷积
        x=self.conv(x)
        # BN
        x=self.bn(x)
        # 激活
        x=self.relu(x)
        # 最大池化
        x=self.mp(x)
        # 残差模块
        x=self.resnet_block1(x)
        x=self.resnet_block2(x)
        x=self.resnet_block3(x)
        x=self.resnet_block4(x)
        # 全局平均池化
        x=self.gap(x)
        # 全链接层
        x=self.fc(x)
        return x
model = ResNet([2,2,2,2])
X = tf.random.uniform((1,224,224,1))
y = model(X)
model.summary()