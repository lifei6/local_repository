import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 1.图像加法
# 读取两张图片
img1 = cv.imread('./image/view.jpg')
img2 = cv.imread('./image/rain.jpg')
# 加法操作
img3 = cv.add(img1,img2) # cv中的加法--饱和赋值为255
img4 = img1 + img2 # numpy中直接相加--取模
# 图像显示--用plt绘图记得翻转rgb--反向读取通道
fig,axes = plt.subplots(1,2,figsize=(10,8),dpi=100)
axes[0].imshow(img3[:,:,::-1])
axes[0].set_title('cv中的加法')
axes[1].imshow(img4[:,:,::-1])
axes[1].set_title('直接相加')
plt.show()
