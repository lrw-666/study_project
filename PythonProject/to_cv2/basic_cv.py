import cv2
import numpy as np
import time

"""图像处理基础操作"""
class draw_cv:
    def __init__(self, image):
        self.img = image
        self.length, self.wight, self.height = self.img.shape
        self.color = (0, 0, 0) # 默认黑色
        self.pointers = []  # 记录当前的像素坐标
        cv2.imshow('img', self.img)
        cv2.waitKey(1)

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
        switch = 'Y'
        cv2.createTrackbar(switch, 'image', 0, 1, self.color_change)
        b, g, r = self.color
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
        cv2.destroyWindow('image')
        self.color = b, g, r
        return b, g, r

    def add_points(self):
        """鼠标点击选取坐标"""
        image = self.img
        self.pointers = [] # 清零
        cv2.namedWindow('draw_image')
        cv2.setMouseCallback('draw_image', self.select_coordinate)
        cv2.destroyWindow('img')
        while True:
            cv2.imshow('draw_image', image)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyWindow('draw_image')
        cv2.imshow('img', self.img)

    def select_coordinate(self, event, x, y, flags, param):
        """鼠标回调事件"""
        if event == cv2.EVENT_LBUTTONDOWN:
            self.pointers.append((x, y))

    def draw_line(self, start, end, thickness=3):
        """绘制一条线，传递线开始和结束坐标"""
        cv2.line(self.img, start, end, self.color, thickness)
        cv2.imshow('img', self.img)

    def draw_rectangle(self, lft, rgt, thickness=3):
        """绘制矩形，需要输入矩形的左上角、右下角和边框厚度（负值填充整个矩形）"""
        cv2.rectangle(self.img, lft, rgt, self.color, thickness)
        cv2.imshow('img', self.img)

    def draw_circle(self, center, r, thickness=-1):
        """绘制圆圈，需要输入中心坐标、半径和粗细（负值填充）"""
        cv2.circle(self.img, center, r, self.color, thickness)
        cv2.imshow('img', self.img)

    def draw_ellipse(self, center, length, angle, start=0, end=360, thickness=-1):
        """绘制椭圆，需要输入中心位置、长轴和短轴长度、沿逆时针选择的角度，主轴沿顺时针方向测量的椭圆弧的开始和结束(0,360表示完整的椭圆)、粗细"""
        cv2.ellipse(self.img, center, length, angle, start, end, self.color, thickness)
        cv2.imshow('img', self.img)

    def draw_polylines(self, points, flag=True, thickness=3):
        """绘制多边形(多条线)，需要输入定点的坐标，flag为False的话就得到一条连接所有点的折线，将这些点组成形状为ROWSx1x2的数组，且类型应该为int32"""
        # 可绘制多条线，创建所有线条的列表传递即可
        points = np.array(points, np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(self.img, [points], flag, self.color, thickness)
        cv2.imshow('img', self.img)

    def draw_Text(self, text, lft, size=4, thickness=3):
        """将文本放入图片，参数:文字、左下角位置、字体类型、大小、颜色、厚度、线条类型"""
        lineType = cv2.LINE_AA # 推荐线条类型
        font = cv2.FONT_HERSHEY_SIMPLEX # 字体
        cv2.putText(self.img, text, lft, font, size, self.color, thickness, lineType)
        cv2.imshow('img', self.img)

if __name__ == '__main__':
    img1 = cv2.imread('001.jpg')
    draw = draw_cv(img1)
    draw.draw_line((0, 0), (500, 500))
    draw.draw_circle((500, 500), 50)
    draw.draw_Text("lrw", (500, 500))
    cv2.imshow('img', draw.img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()