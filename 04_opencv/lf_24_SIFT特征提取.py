# sift提取关键点
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
# 2 sift关键点检测
# 2.1 实例化sift对象
sift = cv.SIFT_create()
# 2.2 关键点检测：kp关键点信息包括方向，尺度，位置信息，des是关键点的描述符
# kp,des = sift.detectAndCompute(gray,None)
kp,des = sift.detectAndCompute(gray,None)
# 2.3 在图像上绘制关键点的检测结果
# cv.drawKeypoints(image, keypoints, outputimage, color, flags)
# image: 原始图像
# keypoints：关键点信息，将其绘制在图像上
# outputimage：输出图片，可以是原始图像
# flags: 绘图功能的标识设置
cv.drawKeypoints(img,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 3 图像显示
plt.figure(figsize=(8,6),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('sift检测')
plt.xticks([]), plt.yticks([])
plt.show()



