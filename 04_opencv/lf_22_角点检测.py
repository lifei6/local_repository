# 这里面特征提取指检测角点
# Harris角点检测
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 1.获取图像
img = cv.imread('./image/chessboard.jpg')
print(img.shape)
# 转为灰度图
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# 2 角点检测
# dst=cv.cornerHarris(src, blockSize, ksize, k)
# img：数据类型为 ﬂoat32 的输入图像。
# blockSize：角点检测中要考虑的邻域大小。
# ksize：sobel求导使用的核大小
# k ：角点检测方程中的自由参数，取值参数为 [0.04，0.06].
# 2.1 输入图像必须是 float32
gray = np.float32(gray)
# 2.2 最后一个参数在 0.04 到 0.06 之间
dst = cv.cornerHarris(gray,2,3,0.04)
print(dst.shape)
# 3 设置阈值，将角点绘制出来，阈值根据图像进行选择
img[dst>0.001*dst.max()] = [0,0,255]
# 4 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('Harris角点检测')
plt.xticks([]), plt.yticks([])
plt.show()
