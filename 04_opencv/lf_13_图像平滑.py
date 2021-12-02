import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 获取图像
img = cv.imread('./image/dogsp.jpeg')
img1 = cv.imread('./image/dogGauss.jpeg')
# 1.均值滤波
# blur = cv.blur(img,(5,5))
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('原图')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur[:,:,::-1]),plt.title('均值滤波后结果')
# plt.xticks([]), plt.yticks([])
# plt.show()

# 2.高斯滤波
blur = cv.GaussianBlur(img1,ksize=(3,3),sigmaX=1,sigmaY=1)
# 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img1[:,:,::-1]),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur[:,:,::-1]),plt.title('高斯滤波后结果')
plt.xticks([]), plt.yticks([])
plt.show()

# 3.中值滤波--对去除椒盐噪声特别好用
# blur = cv.medianBlur(img,ksize=5)
# # 图像展示
# plt.figure(figsize=(10,8),dpi=100)
# plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('原图')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur[:,:,::-1]),plt.title('中值滤波后结果')
# plt.xticks([]), plt.yticks([])
# plt.show()