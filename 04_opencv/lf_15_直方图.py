import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 获取图像
img = cv.imread('./image/cat.jpeg',0)
# 1.直方图
# 统计灰度图
# cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
# histr = cv.calcHist([img],[0],None,[256],[0,256])
# # 绘制灰度图
# plt.figure(figsize=(10,6),dpi=100)
# plt.plot(histr)
# plt.grid()
# plt.show()

# 2.掩膜的应用
# # 2.1 创建蒙板
# mask = np.zeros(img.shape[:2],dtype=np.int8)
# mask[400:650,200:500] = 255
# # 2.2 掩膜
# masked_img = cv.bitwise_and(img,img,mask=mask)
# # 2.3 统计掩膜后的灰度值
# mask_histr = cv.calcHist([img],[0],mask,[256],[1,256])
# # 2.4 绘制直方图
# fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,8))
# axes[0,0].imshow(img,cmap=plt.cm.gray)
# axes[0,0].set_title("原图")
# axes[0,1].imshow(mask,cmap=plt.cm.gray)
# axes[0,1].set_title("蒙版数据")
# axes[1,0].imshow(masked_img,cmap=plt.cm.gray)
# axes[1,0].set_title("掩膜后数据")
# axes[1,1].plot(mask_histr)
# axes[1,1].grid()
# axes[1,1].set_title("灰度直方图")
# plt.show()

# 3.直方图均衡化
# # 2. 均衡化处理
# dst = cv.equalizeHist(img)
# # 结果展示
# plt.imshow(dst,cmap='gray')
# plt.show()

# 4.自适应均衡化
# 创建一个自适应均衡化对象，并运用于图像
# 对比度限制为2.0，分块大小为8*8
clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(img)
# 图像展示
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img,cmap=plt.cm.gray)
axes[0].set_title("原图")
axes[1].imshow(cl1,cmap=plt.cm.gray)
axes[1].set_title("自适应均衡化后的结果")
plt.show()