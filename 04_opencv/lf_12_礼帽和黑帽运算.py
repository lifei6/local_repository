import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 获取图像
img1 = cv.imread('./image/letteropen.png')
img2 = cv.imread('./image/letterclose.png')
# 创建一个10*10的核结构
kernel = np.ones((10,10),np.int8)
# 礼帽运算--原图-开运算图--获取背景--分离比邻近点亮一些的斑块
cvOpen = cv.morphologyEx(img1,op=cv.MORPH_TOPHAT,kernel=kernel)
# 黑帽运算--闭运算图-原图--分离比邻近点暗一些的斑块
cvClose = cv.morphologyEx(img2,op=cv.MORPH_BLACKHAT,kernel=kernel)
# 图像展示
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
axes[0,0].imshow(img1)
axes[0,0].set_title("原图")
axes[0,1].imshow(cvOpen)
axes[0,1].set_title("礼帽运算结果")
axes[1,0].imshow(img2)
axes[1,0].set_title("原图")
axes[1,1].imshow(cvClose)
axes[1,1].set_title("黑帽运算结果")
plt.show()
