# 视频中的人脸识别
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 1.读取视频
cap = cv.VideoCapture('./xiaonanhai.mp4')
# 2.在每一帧图片中进行人脸检测
while(cap.isOpened()):
    # 读取每一帧图像
    ret,frame = cap.read()
    if ret==True:
        # 转为灰度图
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        # 3.实列化人脸识别的分类器
        face_cas = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        face_cas.load('haarcascade_frontalface_default.xml')
        # 4.进行人脸检测返回矩形窗口
        face_rects = face_cas.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))
        # 5.历便所有的人脸窗口，框出人脸
        for facerect in face_rects:
            x,y,w,h = facerect
            # 绘制矩形
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # 6.显示标记人脸后的每一帧1ms一帧
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# 7. 释放资源
cap.release()
cv.destroyAllWindows()
