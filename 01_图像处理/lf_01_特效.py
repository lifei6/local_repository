import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
"""
Author:lifei
date:2021/11/28
"""


# 毛玻璃特效
def maoBoLi(img0):
    """
    当前的像素点的邻域内随机取一个像素点来代替它
    :param img0: 原图
    """
    img2 = np.zeros((h, w, 3), np.uint8)  # 生成与原图像等大的全零矩阵
    for i in range(0, h - 6):  # 防止下面的随机数超出边缘
        for j in range(0, w - 6):
            index = int(np.random.random() * 6)  # 0~6的随机数
            (b, g, r) = img0[i + index, j + index]
            img2[i, j] = (b, g, r)
    cv2.imshow("W2", img2[:h-6, :w-6])
    cv2.waitKey(delay=0)


# 浮雕特效
def fuDiao(img1):
    # 浮雕特效(需要对灰度图像进行操作)
    img3 = np.zeros((h, w, 3), np.uint8)
    for i in range(0, h):
        for j in range(0, w - 2):  # 减2的效果和上面一样
            grayP0 = int(img1[i, j])
            grayP1 = int(img1[i, j + 2])  # 取与前一个像素点相邻的点
            newP = grayP0 - grayP1 + 150  # 得到差值，加一个常数可以增加浮雕立体感
            if newP > 255:
                newP = 255
            if newP < 0:
                newP = 0
            img3[i, j] = newP
    cv2.imshow("W3", img3)
    cv2.waitKey(delay=0)


# 素描特效
def suMiao(img1):
    # 素描特效
    img4 = 255 - img1  # 对原灰度图像的像素点进行反转
    blurred = cv2.GaussianBlur(img4, (21, 21), 0)  # 进行高斯模糊
    inverted_blurred = 255 - blurred  # 反转
    img4 = cv2.divide(img1, inverted_blurred, scale=127.0)  # 灰度图像除以倒置的模糊图像得到铅笔素描画
    cv2.imshow("W4", img4)
    cv2.waitKey(delay=0)


# 怀旧特效
def huaiJiu(img0):
    # 怀旧特效
    img5 = np.zeros((h, w, 3), np.uint8)
    for i in range(0, h):
        for j in range(0, w):
            B = 0.272 * img0[i, j][2] + 0.534 * img0[i, j][1] + 0.131 * img0[i, j][0]
            G = 0.349 * img0[i, j][2] + 0.686 * img0[i, j][1] + 0.168 * img0[i, j][0]
            R = 0.393 * img0[i, j][2] + 0.769 * img0[i, j][1] + 0.189 * img0[i, j][0]
            if B > 255:
                B = 255
            if G > 255:
                G = 255
            if R > 255:
                R = 255
            img5[i, j] = np.uint8((B, G, R))
    cv2.imshow("W5", img5)
    cv2.waitKey(delay=0)


# 流年特效
def liuNian(img0):
    # 流年特效
    img6 = np.zeros((h, w, 3), np.uint8)
    for i in range(0, h):
        for j in range(0, w):
            B = math.sqrt(img0[i, j][0]) * 14  # B通道的数值开平方乘以参数14
            G = img0[i, j][1]
            R = img0[i, j][2]
            if B > 255:
                B = 255
            img6[i, j] = np.uint8((B, G, R))
    cv2.imshow("W6", img6)
    cv2.waitKey(delay=0)


# 水波特效
def shuiBo(img0):
    # 水波特效
    img7 = np.zeros((h, w, 3), np.uint8)
    wavelength = 20  # 定义水波特效波长
    amplitude = 30  # 幅度
    phase = math.pi / 4  # 相位
    centreX = 0.5  # 水波中心点X
    centreY = 0.5  # 水波中心点Y
    radius = min(h, w) / 2
    icentreX = w * centreX  # 水波覆盖宽度
    icentreY = h * centreY  # 水波覆盖高度
    for i in range(0, h):
        for j in range(0, w):
            dx = j - icentreX
            dy = i - icentreY
            distance = dx * dx + dy * dy
            if distance > radius * radius:
                x = j
                y = i
            else:
                # 计算水波区域
                distance = math.sqrt(distance)
                amount = amplitude * math.sin(distance / wavelength * 2 * math.pi - phase)
                amount = amount * (radius - distance) / radius
                amount = amount * wavelength / (distance + 0.0001)
                x = j + dx * amount
                y = i + dy * amount
            # 边界判断
            if x < 0:
                x = 0
            if x >= w - 1:
                x = w - 2
            if y < 0:
                y = 0
            if y >= h - 1:
                y = h - 2
            p = x - int(x)
            q = y - int(y)
            # 图像水波赋值
            img7[i, j, :] = (1 - p) * (1 - q) * img0[int(y), int(x), :] + p * (1 - q) * img0[int(y), int(x), :]
            + (1 - p) * q * img0[int(y), int(x), :] + p * q * img0[int(y), int(x), :]
    cv2.imshow("W7", img7)
    cv2.waitKey(delay=0)


# 卡通特效
def kaTong(img0):
    # 卡通特效
    num_bilateral = 7  # 定义双边滤波的数目
    for i in range(num_bilateral):  # 双边滤波处理，除去噪声，保留边界
        img_color = cv2.bilateralFilter(img0, d=9, sigmaColor=5, sigmaSpace=3)
    img_blur = cv2.medianBlur(img1, 7)  # 中值滤波处理
    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=5,
                                     C=2)  # 边缘检测及自适应阈值化处理，提取边界
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)  # 转换回彩色图像
    img8 = cv2.bitwise_and(img0, img_edge)  # 图像的与运算
    cv2.imshow('W8', img8)
    cv2.waitKey(delay=0)


if __name__ == '__main__':
    # 读取图片转为灰度图
    img0 = cv2.imread('./imagedata/meinv.png')
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    h, w = img0.shape[:2]
    print("图片的高和宽为：", h, w)
    # 毛玻璃特效
    # maoBoLi(img0)
    # 浮雕特效
    # fuDiao(img1)
    # 素描特效
    # suMiao(img1)
    # 怀旧特效
    # huaiJiu(img0)
    # 流年特效
    # liuNian(img0)
    # 水波特效
    # shuiBo(img0)
    # 卡通特效
    kaTong(img0)


