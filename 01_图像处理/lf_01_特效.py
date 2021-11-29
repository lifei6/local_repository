import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
Author:lifei
date:2021/11/28
"""
# 毛玻璃特效
img = cv2.imread('./imagedata/meinv.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h,w = img.shape[:2]
print("图片的高和宽为：", h, w)
cv2.imshow("W0",img)
cv2.imshow("W1",img1)
cv2.waitKey(delay=0)


