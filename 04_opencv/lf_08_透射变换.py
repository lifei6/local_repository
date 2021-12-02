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
# 透射变换
# 获得透射矩阵
rows,cols = img1.shape[:2]
# 透射前的点坐标
vct1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# 透射后的点坐标
vct2 = np.float32([[100,145],[300,100],[80,290],[310,300]])
T = cv.getPerspectiveTransform(vct1,vct2)
# 调用方法
img2 = cv.warpPerspective(img1,T,(2*cols,2*rows))
# 显示图片
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img1[:,:,::-1])
axes[0].set_title("原图")
axes[1].imshow(img2[:,:,::-1])
axes[1].set_title("透射后结果")
plt.show()