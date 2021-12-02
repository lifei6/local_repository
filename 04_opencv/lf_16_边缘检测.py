# sobel算子和scharr算子
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

# 3.计算Sobel卷积结果
# Sobel_x_or_y = cv2.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
x = cv.Sobel(img,cv.CV_16S,1,0,ksize=3)
y = cv.Sobel(img,cv.CV_16S,0,1,ksize=3)
# 4.将数据进行转化16-->unit8--才能正常显示
Scale_absX = cv.convertScaleAbs(x)
Scale_absY = cv.convertScaleAbs(y)
# 5.结果合成
result = cv.addWeighted(Scale_absX,0.5,Scale_absY,0.5,0)
# 6.显示图像
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(result,cmap = plt.cm.gray),plt.title('Sobel滤波后结果')
plt.xticks([]), plt.yticks([])
plt.show()


# 将上述代码中计算sobel算子的部分中将ksize设为-1，就是利用Scharr进行边缘检测。
# x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize = -1)
# y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize = -1)