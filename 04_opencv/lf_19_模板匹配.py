# 1.模块导入
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 获取图片和模板图片
img = cv.imread('./image/wulin.jpeg')
template = cv.imread('./image/bai.jpeg')
h,w,l = template.shape
print((h,w,l))
# 1.进行模板匹配--采用相关匹配
# res = cv.matchTemplate(img,template,method)
# 平方差匹配(cv.TM_SQDIFF) 相关匹配(cv.TM_CCORR) 利用相关系数匹配(cv.TM_CCOEFF)
res = cv.matchTemplate(img,template,cv.TM_CCORR)
# 2.返回图像中最匹配的位置，确定左上角的坐标，并将匹配位置绘制在图像上
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)
# 使用平方差时最小值为最佳匹配位置
# top_left = min_loc
top_left = max_loc
print(max_loc)
botton_right = (top_left[0]+w,top_left[1]+h)
cv.rectangle(img,top_left,botton_right,(255,0,0),2)
# 3 图像显示
plt.imshow(img[:,:,::-1])
plt.title('匹配结果'), plt.xticks([]), plt.yticks([])
plt.show()


