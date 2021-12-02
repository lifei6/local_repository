# fast提取关键点
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
# 2 Fast角点检测
# 2.1 实例化一个检测器,传入阈值，默认开启非极大值抑制注意：可以处理彩色图像
fast = cv.FastFeatureDetector_create(threshold=30)
# 2.2 检测图像上的关键点
kp = fast.detect(img,None)
# 2.3.在图像上绘制关键点
img2 = cv.drawKeypoints(img,kp,None,(0,0,255))
# 2.4.输出默认参数
print("Threshold: {}".format(fast.getThreshold()))
print("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
print("neighborhood: {}".format(fast.getType()))
print("total keypoints with nonmaxsuppression: {}".format(len(kp)))
# 2.5 关闭非极大值抑制
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)
print("total keypoints with nonmaxsuppression: {}".format(len(kp)))
# 2.6 绘制为进行非极大值抑制的结果
img3 = cv.drawKeypoints(img,kp,None,(0,0,255))
# 3 绘制图像
fig,axes = plt.subplots(1,2,figsize=(10,8),dpi=100)
axes[0].imshow(img2[:,:,::-1])
axes[0].set_title("加入非极大值抑制")
axes[1].imshow(img3[:,:,::-1])
axes[1].set_title("未加入非极大值抑制")
plt.show()