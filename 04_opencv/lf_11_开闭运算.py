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
# 开运算--先腐蚀再膨胀--消除外部噪点
cvOpen = cv.morphologyEx(img1,op=cv.MORPH_OPEN,kernel=kernel)
# 闭运算--先膨胀再腐蚀--消除内部空洞
cvClose = cv.morphologyEx(img2,op=cv.MORPH_CLOSE,kernel=kernel)
# 图像展示
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
axes[0,0].imshow(img1)
axes[0,0].set_title("原图")
axes[0,1].imshow(cvOpen)
axes[0,1].set_title("开运算结果")
axes[1,0].imshow(img2)
axes[1,0].set_title("原图")
axes[1,1].imshow(cvClose)
axes[1,1].set_title("闭运算结果")
plt.show()

