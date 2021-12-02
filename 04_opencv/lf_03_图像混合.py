import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 1.图像混合
# 读取两张图片
img1 = cv.imread('./image/view.jpg')
img2 = cv.imread('./image/rain.jpg')
# 混合运算
img = cv.addWeighted(img1,0.7,img2,0.3,0)
# 图像显示
plt.figure(figsize=(8,8))
plt.imshow(img[:,:,::-1])
plt.show()