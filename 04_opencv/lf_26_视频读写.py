import numpy as np
import cv2 as cv
# 1 读取视频
cap = cv.VideoCapture('./image/DOG.wmv')
# 2 判断是否读取成功
while(cap.isOpened()):
    # 3 获取每一帧图像
    ret,frame=cap.read()
    # 4 获取成功显示图像
    if ret == True:
        cv.imshow('frame',frame)
    # 5 每一帧时隔为25ms
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
# 6.释放视频对象
cap.release()
cv.destoryAllwindows()

