import cv2
import numpy as np
import time

"""图像处理基础操作"""
class draw_cv:
    def __init__(self):
        self.length = 512
        self.wight = 512
        self.height = 3
        self.color = (0, 0, 0) # 默认黑色

    def __repr__(self):
        return "进行cv绘图功能的类"

    @property
    def size(self):
        """获取属性size"""
        return self.length, self.wight, self.height

    @size.setter
    def size(self, size):
        """设置属性size"""
        self.length, self.wight, self.height = size

    def color_change(self, x):
        """设置当前颜色"""
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        self.color = (b, g, r)

    def color_palette(self):
        """调色板"""
        size = (150, 512, 3)
        img = np.zeros(size, np.uint8) # 建立一个纯黑的画板
        cv2.namedWindow('image')
        cv2.createTrackbar('R', 'image', 0, 255, self.color_change)
        cv2.createTrackbar('G', 'image', 0, 255, self.color_change)
        cv2.createTrackbar('B', 'image', 0, 255, self.color_change)
        switch = '0:OFF 1:ON'
        cv2.createTrackbar(switch, 'image', 0, 1, self.color_change)
        while True:
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF # & 0xFF的按位与操作只取cv2.waitKey(1)返回值最后八位，因为有些系统cv2.waitKey(1)的返回值不止八位
            if k == 27:
                break
            r = cv2.getTrackbarPos('R', 'image')
            g = cv2.getTrackbarPos('G', 'image')
            b = cv2.getTrackbarPos('B', 'image')
            s = cv2.getTrackbarPos(switch, 'image')
            if s == 0:
                img[:] = 0
            else:
                img[:] = [b, g, r]
        cv2.destroyAllWindows()

if __name__ == '__main__':
    draw = draw_cv()
    draw.color_palette()