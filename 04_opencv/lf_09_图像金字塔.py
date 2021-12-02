import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 获取图像
img1 = cv.imread('./image/kids.jpg')
# 1.上采样
img_up = cv.pyrUp(img1)
# 2.下采样
img_down = cv.pyrDown(img1)
# 显示图片
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(20,8),dpi=100)
axes[0].imshow(img1[:,:,::-1])
axes[0].set_title("原图")
axes[1].imshow(img_up[:,:,::-1])
axes[1].set_title("上采样后结果")
axes[2].imshow(img_down[:,:,::-1])
axes[2].set_title("下采样后结果")
plt.show()