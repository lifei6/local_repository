import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 获取图像
img = cv.imread('./image/rili.jpg')
# 图像二值化
# 1.获取灰度图
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 2.边缘检测获取二值点
edges = cv.Canny(gray,50,150)

# 霍夫直线变化
# cv.HoughLines(img, rho, theta, threshold)
# img: 检测的图像，要求是二值化的图像，所以在调用霍夫变换之前首先要进行二值化，或者进行Canny边缘检测
# rho、theta: ρ和θ的精确度
# threshold: 阈值，只有累加器中的值高于该阈值时才被认为是直线。
# 返回的线是极坐标的形式（ρ，θ）
lines = cv.HoughLines(edges,0.8,np.pi / 180,200)
print(lines)
# 将检测的线绘制在图像上（注意是极坐标噢）--绘制图像的y轴与笛卡尔坐标系的y轴反向
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho*a
    y0 = rho*b
    # why?????
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    # 在图像上标出直线
    cv.line(img,(x1,y1),(x2,y2),(0,255,0))
# 4. 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('霍夫变换线检测')
plt.xticks([]), plt.yticks([])
plt.show()