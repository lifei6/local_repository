# M = cv2.getRotationMatrix2D(center, angle, scale)
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
# 图像旋转
# 旋转矩阵M
rows,cols = img1.shape[:2]
M = cv.getRotationMatrix2D(center=(rows/2,cols/2),angle=45,scale=0.5)
img2 = cv.warpAffine(img1,M,(2*cols,2*rows))
# 显示图片
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img1[:,:,::-1])
axes[0].set_title("原图")
axes[1].imshow(img2[:,:,::-1])
axes[1].set_title("旋转45度后结果")
plt.show()