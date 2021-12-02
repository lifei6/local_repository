# cifar10和cifar100数据集的导入
import tensorflow as tf
from tensorflow.keras.datasets import cifar10,cifar100
# 加载cifar10图片数据
(train_images,train_labels),(test_images,test_labels) = cifar10.load_data()
print(train_images.shape)
print(train_labels[1])
# 加载cifar100图片数据
(train_images1,train_labels1),(test_images1,test_labels1) = cifar100.load_data()
print(train_images1.shape)
print(train_labels1[1])