# 案例一：利用OpenCV实现图像校正
import cv2
import numpy as np
import math

im1 = cv2.imread('001.png')
im = cv2.resize(im1, (500, 300), interpolation=cv2.INTER_NEAREST)  # 最近邻插值
cv2.imshow('im', im)
# 灰度化
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# 二值化效果不佳,改变策略
# t, im_binary = cv2.threshold(im_gray, 200, 255, cv2.THRESH_OTSU)
# cv2.imshow('im_binary', im_binary)

# 边缘提取
# sobel = cv2.Sobel(im_gray, cv2.CV_64F, 1, 1, ksize=5)
# cv2.imshow('sobel', sobel)
# 有小点，效果也不行，再换

# Laplacian边缘提取
# lap = cv2.Laplacian(im_gray, cv2.CV_64F)
# cv2.imshow('lap', lap)
# 效果也不行，再换

# 模糊化
blurred = cv2.GaussianBlur(im_gray, (5, 5), 0)
# 膨胀
dilate = cv2.dilate(blurred, (3, 3))

# Canny边缘提取
canny = cv2.Canny(im, 50, 200)  # 效果很好， 下一步操作：加上模糊化处理和膨胀,轮廓检测
cv2.imshow('canny', canny)

# 轮廓检测
cnts, hie = cv2.findContours(canny.copy(),  # 原始图像
                             cv2.RETR_EXTERNAL,  # 只检测外轮廓
                             cv2.CHAIN_APPROX_SIMPLE)  # 只保留轮廓终点坐标
# 绘制轮廓
im_cnt = cv2.drawContours(im, cnts, -1, (0, 0, 255), 2)
cv2.imshow('im_cnt', im_cnt)

# 计算轮廓面积，排序
if len(cnts) > 0:
    cnts = sorted(cnts,  # 可迭代对象
                  key=cv2.contourArea,  # 计算轮廓面积，根据面积排序
                  reverse=True)  # 逆序排列
    for c in cnts:  # 遍历
        peri = cv2.arcLength(c, True)  # 计算封闭轮廓周长
        approx = cv2.approxPolyDP(c, 0.1 * peri, True)  # 多边形拟合
        # 拟合出的第一个四边形认为是纸张的轮廓
        if len(approx) == 4:
            docCnt = approx
            break

# 绘制找到的四边形的交点
points = []
for peak in docCnt:
    peak = peak[0]  # 取出坐标
    # 绘制角点
    cv2.circle(im,  # 绘制的图像
               tuple(peak), 20,  # 圆心、半径
               (0, 0, 255), 2)  # 绘制圆形线条颜色、粗细
    points.append(peak)  # 坐标添加到列表
cv2.imshow('im_point', im)

# 校正
# 原纸张逆时针方向四个角点
src = np.float32([points[0], points[1], points[2], points[3]])
dst = np.float32([[0, 0], [0, 488], [337, 488], [337, 0]])
m = cv2.getPerspectiveTransform(src, dst) # 生成透视矩阵
result = cv2.warpPerspective(im_gray.copy(), m, (337, 488)) # 透视变换

# 根据勾股定理计算宽度、高度，再做透视变换
# h = int(math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2))
# w = int(math.sqrt((points[2][0] - points[1][0])**2 + (points[2][1] - points[1][1])**2))
# dst = np.float32([[0, 0], [0, h], [w, h], [w, 0]])
# m = cv2.getPerspectiveTransform(src, dst)
# result = cv2.warpPerspective(im_gray.copy(), m, (w, h))

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
局限：对多边形拟合那里要求很高，使用场景苛刻
"""