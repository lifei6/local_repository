import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 读取图片
img = cv.imread('./image/littledog.jpeg')
# 图像缩放
# 1.绝对尺寸
rows,cols = img.shape[:2]
img1 = cv.resize(img,dsize=(rows*2,cols*2),interpolation=cv.INTER_CUBIC)
# 2.相对尺寸
img2 = cv.resize(img,dsize=None,fx=0.5,fy=0.5)

# 3.图片显示
fig,axes = plt.subplots(1,3,figsize=(20,8))
axes[0].imshow(img1[:,:,::-1])
axes[0].set_title('enlarge')
axes[1].imshow(img[:,:,::-1])
axes[1].set_title('orignal')
axes[2].imshow(img2[:,:,::-1])
axes[2].set_title('shrink')
plt.show()