# 使用OpenCV实现图像覆盖
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('001.jpeg')
# 将BGR格式转化为RGB格式的方法(OpenCV以BGR格式读取图像)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('img1', img_rgb)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img2', img_gray)

# 改变图像某一区域的像素值
img[50:100, 50:100] = [100, 0, 0]
cv2.imshow('img', img)

# 将覆盖图像修改为要替换的像素值的大小
img2 = cv2.imread('002.jpg')
resized_img = cv2.resize(img2, dsize=(100, 100))
img[50:150, 50:150] = resized_img
cv2.imshow('img', img)

# 覆盖PNG图像：与JPEG图像不同，PGN图像有四个通道，定义了给定像素的ALPHA(不透明度)，需要以规定方式读取
# 读取时指定标志cv2.IMREAD_UNCHANGED，图像有四个通道：BGRA, 不能简单的替换值
img3 = cv2.imread('003.png', cv2.IMREAD_UNCHANGED)
# numpy提供了一个函数dstack()来根据深度叠加值
# 创建虚拟通道
img = cv2.imread('001.jpeg')
img3 = cv2.resize(img3, (100, 100))
ones = np.ones((img.shape[0], img.shape[1]))*255 # alpha通道的值也存在与0-255之间
img = np.dstack([img, ones])
ones = np.ones(img3.shape[0], img3.shape[1])
# 替换
img[50: 150, 50:150, ] = img3

cv2.waitKey(0)
cv2.destroyAllWindows()
