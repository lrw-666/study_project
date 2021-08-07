# 用OpenCV进行颜色分割
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('001.jpg')
# 使用滤波器对图像进行模糊操作，以减少图像中的细微差异
# 四个内置滤波器：
blur = cv2.blur(img, (5, 5))
blur0 = cv2.medianBlur(blur, 5)
blur1 = cv2.GaussianBlur(blur0, (5, 5), 0)
blur2 = cv2.bilateralFilter(blur1, 9, 75, 75)

# cv2.imshow("滤波", blur2)

# 将图像从BGR(蓝、绿、红)转换到HSV(色相，饱和度，值)，以便于准确描述像素的亮度，饱和度和色度
hsv = cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)
# 颜色分割最重要的一步：阈值分割（参数为HSV描述）
low = np.array([59, 0, 0])
high = np.array([150, 255, 255])
mask = cv2.inRange(hsv, low, high) # 将所有不在描述范围内的其他像素进行覆盖
cv2.imshow("mask", mask)

res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()