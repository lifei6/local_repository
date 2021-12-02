import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 获取图片
img1 = cv.imread('./image/letter.png')
# 创建5*5的核结构
kernel = np.ones((5,5),np.int8)
# 1.图片腐蚀
erosion = cv.erode(img1, kernel,1) # 1为腐蚀次数
# 2.图片膨胀
dilate = cv.dilate(img1,kernel,1)
# 图像显示
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
axes[0].imshow(img1)
axes[0].set_title("原图")
axes[1].imshow(erosion)
axes[1].set_title("腐蚀后结果")
axes[2].imshow(dilate)
axes[2].set_title("膨胀后结果")
plt.show()