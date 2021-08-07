import cv2
# Python图像处理类库(其中最重要的是Image)
from PIL import Image

# Matplotlib()：处理数学运算、绘制图表、在图像上绘制点、直线和曲线的类库
from pylab import *
# im = array(Image.open("002.jpg"))
# imshow(im)
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]
# plot(x, y, 'r*')
# plot(x[:2], y[:2])
# title('Plotting: "empire.jpg"')
# axis('off')
# show()

# Numpy包：Python科学计算工具包
import numpy as np
im = array(Image.open("002.jpg"))
print(im.shape, im.dtype)
im = array(Image.open('002.jpg').convert('L'), 'f')
print(im.shape, im.dtype)

im = array(Image.open('002.jpg').convert('L'))
im2 = 255 - im  # 对图像进行反相处理
im3 = (100.0/255) * im + 100 # 将图像像素变换到100...200间
im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到图像
pil_im = Image.fromarray(uint8(im)) # array()变换的相反操作，有时需要先转换为uint8数据类型
print(im.shape, im.dtype)
cv2.imshow('hh', im)
cv2.waitKey(0)
cv2.destroyAllWindows()

import pickle
# pickle模块:保存一些结果或者数据以方便后续使用
# pickle模块可以接受几乎所有的Python对象，并将其转换成字符串表示，该过程称为封装
# 从字符串中表示重构该对象，称为拆封

# SciPy是建立在Numpy基础上，用于数值运算的开源工具包。

# JSON是用于网络服务间数据传输的常用公式

# PyOpenGL：OpenGL图形编程的Python绑定接口