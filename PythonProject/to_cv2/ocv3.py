# 检测芯片瑕疵
import math

import cv2
import numpy as np

im = cv2.imread('003.png')
cv2.imshow('im', im)
# 灰度化
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('im_gray', im_gray) # 发现亮度很明显，二值化

# 二值化
ret, im_bin = cv2.threshold(im_gray, 160, 255, cv2.THRESH_BINARY) # 默认127，根据实际调整
cv2.imshow('im_bin', im_bin)

# 提取轮廓，实心化填充
cnts, hie = cv2.findContours(im_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
mask = np.zeros(im_bin.shape, np.uint8) # 创建值全为0的矩阵，形状和im_bin一致
im_fill = cv2.drawContours(mask, cnts, -1, (255, 0, 0), -1) # 绘制轮廓并进行实心填充
cv2.imshow('im_fill', im_fill)
# 图像减法，找出瑕疵区域
im_sub = cv2.subtract(im_fill, im_bin)
cv2.imshow('im_sub', im_sub)
# 图像的逆运算（先膨胀后腐蚀），将离散的瑕疵点合并在一起
k = np.ones((10, 10), np.uint8)
im_close = cv2.morphologyEx(im_sub, cv2.MORPH_CLOSE, k, iterations=3)
# 产生最小外接圆数据
im_show = cv2.drawContours(im_close.copy(), cnts[0],  -1, (0, 0, 255), 2)
cv2.imshow("hh", im_show)
(x, y), radius = cv2.minEnclosingCircle(cnts[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(im_close, center, radius, (255, 0, 0), 2) # 绘制瑕疵最小外接圆形
cv2.imshow('im_circle', im_close)
# 在原始图像上绘制
cv2.circle(im, center, radius, (0, 0, 255), 2)
cv2.imshow('im_result', im)
# 计算外接圆面积
area = math.pi * radius * radius
print("area:", area)
if area > 12:
    print("度盘表面有瑕疵")

cv2.waitKey(0)
cv2.destroyAllWindows()