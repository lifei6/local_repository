# 图像中的人脸识别
import cv2 as cv
import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 1 获取图片转为灰度图
img = cv.imread('./image/yangzi.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 2.实例化OpenCV人脸和眼睛识别的分类器
# 实例化人脸的
face_cas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
# 加载模型
face_cas.load("haarcascade_frontalface_default.xml")
# 实例化眼睛的
eyes_cas = cv.CascadeClassifier("haarcascade_eye.xml")
eyes_cas.load("haarcascade_eye.xml")
# 3.调用识别人脸
face_rects = face_cas.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32, 32))
# 遍历所有的人脸矩阵
for facerect in face_rects:
    x,y,w,h = facerect
    # 框出人脸
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    # 4.在识别出的人脸中进行眼睛的检测
    roi_color = img[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w]
    eye_rects = eyes_cas.detectMultiScale(roi_gray)
    for eye in eye_rects:
        ex,ey,ew,eh = eye
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
# 5. 检测结果的绘制
plt.figure(figsize=(8,6),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('检测结果')
plt.xticks([]), plt.yticks([])
plt.show()
