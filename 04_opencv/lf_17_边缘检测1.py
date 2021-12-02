# laplacian算子
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

# 3.laplacian转化
result = cv.Laplacian(img,cv.CV_16S,ksize=3)

# 4.进行结构转化
Scale_abs = cv.convertScaleAbs(result)

# 5.显示图像
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(Scale_abs,cmap = plt.cm.gray),plt.title('Laplacian检测后结果')
plt.xticks([]), plt.yticks([])
plt.show()