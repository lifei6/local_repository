# shi-Tomasi角点检测
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 1.获取图片
img = cv.imread('./image/tv.jpg')
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# 2.shi-Tomasi角点检测
corners = cv.goodFeaturesToTrack(gray,1000,0.01,10)
print(corners)
# 3.绘制角点
for i in corners:
    print(i)
    x,y = i.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,0,255),-1)
# 4 图像展示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('shi-tomasi角点检测')
plt.xticks([]), plt.yticks([])
plt.show()
