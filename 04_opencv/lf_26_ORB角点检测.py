# ORB提取关键点
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 1 获取图片
img = cv.imread('./image/tv.jpg')
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# 2 orb关键点检测
# 2.1 实例化orb对象
orb = cv.ORB_create(nfeatures=500)
# 2.2 关键点检测：kp关键点信息包括方向，尺度，位置信息，des是关键点的描述符
kp,des = orb.detectAndCompute(img,None)
print(des.shape)
# 2.3 在图像上绘制关键点的检测结果
img1 = cv.drawKeypoints(img,kp,None,(0,0,255))
# 3 图像显示
plt.figure(figsize=(8,6),dpi=100)
plt.imshow(img1[:,:,::-1]),plt.title('ORB检测')
plt.xticks([]), plt.yticks([])
plt.show()