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
# 图像平移
# 平移矩阵
rows,cols = img1.shape[:2]
M = np.array([[1,0,100],[0,1,50]],dtype=np.float32)
print(M)
# 注意：输出图像的大小，它应该是(宽度，高度)的形式。请记住,width=列数，height=行数。
dst = cv.warpAffine(img1,M,dsize=(2*cols,2*rows))
# 显示图片
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img1[:,:,::-1])
axes[0].set_title("原图")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("平移后结果")
plt.show()