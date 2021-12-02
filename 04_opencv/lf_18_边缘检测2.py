# canny边缘检测
# 1.模块导入
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 2.获取灰度图像
img = cv.imread('./image/horse.jpg',0)

# 3.进行高斯滤波
blur = cv.GaussianBlur(img,ksize=(3,3),sigmaX=1,sigmaY=1)

# 4.canny检测
# canny = cv2.Canny(image, threshold1, threshold2) 第一个为最小阈值，第二个为最大阈值
result = cv.Canny(blur,0,100)
# 5.图像展示
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(result,cmap = plt.cm.gray),plt.title('Canny检测后结果')
plt.xticks([]), plt.yticks([])
plt.show()