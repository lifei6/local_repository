import cv2
import matplotlib.pyplot as plt
import numpy as np
# 1.读取一个图片
# 1彩色图 0灰度图 -1读取alpha通道
lena = cv2.imread('./cat1.jpg',1)
# 2.显示图片
# 2.1 cv中的方法显示
# str可以设置显示图片的名称
# cv2.imshow('cat',lena)
# cv2.waitKey(0)
# 2.2 以matplotlib中的方法显示
# 在cv中是bgr存储 在plt中是rgb,所以先翻转
# plt.imshow(lena,cmap=plt.cm.gray)
# plt.show()
# 3.图片保存
# cv2.imwrite('cat2.png',lena)
# 4.绘制图像用matlab
# 5.获取并修改图像中的像素
# 获取某个像素点的值
px = lena[100,100]
print("某点的像素值：",px)
# 仅获取蓝色通道的强度值
blue = lena[100,100,0]
print("某点蓝色通道的像素值：",blue)
# 修改某个位置的像素值
lena[100,100] = [255,255,255]
print("修改后的像素值：", lena[100,100])
# 获取图像的属性
print("图像的大小为：",lena.shape)
print("图像的类型：", lena.dtype)
print("图像的像素个数：", lena.size)
# 6.通道拆分与合并
b,g,r = cv2.split(lena)
print("拆分后每个通道的形状：",(b.shape,g.shape,r.shape))
img = cv2.merge((b,g,r))
# cv2.imshow("image",img)
# cv2.waitKey(0)
# 7.色彩空间的改变
# cv2.COLOR_BGR2GRAY/cv2.COLOR_BGR2HSV
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("image",img3)
cv2.waitKey(0)