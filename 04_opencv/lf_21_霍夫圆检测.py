import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 获取图像并转为灰度图
planets = cv.imread('./image/star.jpeg')
gray = cv.cvtColor(planets,cv.COLOR_RGB2GRAY)
# 进行中值滤波
img = cv.medianBlur(gray,7)
# 霍夫圆检测
# circles = cv.HoughCircles(image, method, dp, minDist, param1=100, param2=100, minRadius=0,maxRadius=0 )
# image：输入图像，应输入灰度图像
# method：使用霍夫变换圆检测的算法，它的参数是CV_HOUGH_GRADIENT
# dp：霍夫空间的分辨率，dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推
# minDist为圆心之间的最小距离，如果检测到的两个圆心之间距离小于该值，则认为它们是同一个圆心
# param1：边缘检测时使用Canny算子的高阈值，低阈值是高阈值的一半。
# param2：检测圆心和确定半径时所共有的阈值
# minRadius和maxRadius为所检测到的圆半径的最小值和最大值
# 返回：
# circles：输出圆向量，包括三个浮点型的元素——圆心横坐标，圆心纵坐标和圆半径
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,200,param1=100,param2=30,minRadius=0,maxRadius=100)
print(circles[0,:])
# 4 将检测结果绘制在图像上
for i in circles[0, :]:  # 遍历矩阵每一行的数据

    # 绘制圆形
    cv.circle(planets, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), 2)
    # 绘制圆心
    cv.circle(planets,(int(i[0]), int(i[1])), 2, (0, 0, 255), 3)
# 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(planets[:,:,::-1]),plt.title('霍夫变换圆检测')
plt.xticks([]), plt.yticks([])
plt.show()