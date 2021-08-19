import tkinter as tk
import tkinter.filedialog
import tkinter.font as tkFont
from tkinter.messagebox import showinfo, showwarning, showerror, askokcancel
import os
import re
from functools import partial as pto
import cv2
import shutil

from to_cv2.basic_cv import *

"""用户的可视化界面"""


# 类函数装饰器要写在类外面
def update_photo(action='添加'):
    """用于加入每个图像处理按钮的装饰器（带操作参数）"""

    def outer(func):
        def inner(self, *args, **kwargs):
            self.photo_flag = True
            self.present_action = action
            self.last["text"] = action
            func(self, *args, **kwargs)

        return inner

    return outer

# 定义主框架
class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('图像处理')  # 框名
        self.resizable(1, 0)  # 框体大小可调，分别为x，y方向的可变性
        self.geometry('480x550')  # 主框体大小
        self.fileName = '001.jpg'  # 图片文件名
        self.img = cv2.imread(self.fileName)  # 设置默认图片(此时正在处理的图像)
        self.imgList = [(self.img, '添加'), ]  # 初始化图片列表
        self.photoId = 0  # 记录当前显示原图片
        self.photo_flag = False  # true表示存在正在处理中的图片（未保存）
        self.present_photo = self.img.copy()  # 当前正在处理的图片
        self.present_action = '添加'  # 最近进行的操作
        self.label = tk.Label(text='001.jpg')  # 图片路径标签
        self.name = tk.Label(text=self.fileName)  # 图片文件名标签
        self.size = tk.Label(text=str(self.img.shape))  # 图片尺寸标签
        self.last = tk.Label(text='添加')  # 记录上一步进行的操作的标签
        self.__add_cpt()  # 添加组件与事件

    def __repr__(self):
        """丰富打印内容"""
        actions = []
        for action in self.imgList:
            actions.append(action[1])
        return "%s \n当前图片名:%s \n当前图片大小:%s \n进行的操作:%s" % (
            self.__class__.__name__, self.fileName, str(self.img.shape), actions)

    def __add_cpt(self):
        """初始化组件"""
        # 设置字体
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        ft1 = tkFont.Font(size=15, slant=tkFont.ITALIC)
        # 设置标签
        tk.Label(self, text='先选择图片，再进行操作', font=ft1).grid(row=0, column=0, columnspan=3, padx=10, pady=5,
                                                          sticky='w')  # 设置提示标签,文字左对齐
        self.label = tk.Label(self, text='路径:001.jpg', font=ft)  # 图片路径
        self.label.grid(row=1, column=0, padx=5, pady=5, columnspan=4, sticky='w')  # 跨越四格
        self.name = tk.Label(self, text=self.fileName, font=ft)
        self.name.grid(row=3, column=0, columnspan=1, padx=10, pady=5, sticky='w')  # 图片名称
        self.size = tk.Label(self, text=str(self.img.shape), font=ft)
        self.size.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky='w')  # 图片尺寸
        self.last = tk.Label(self, text='添加', font=ft)
        self.last.grid(row=3, column=2, columnspan=1, padx=10, pady=5, sticky='w')  # 图片最近操作

        # 定义各类按钮
        tk.Button(self, text='->选择图片', font=ft1,
                  command=self.photo_file).grid(row=0, column=3, columnspan=1, padx=10, pady=5, sticky='w')  # 图片选择按钮
        tk.Button(self, font=ft1, text='上一步', command=self.last_photo).grid(
            row=2, column=0, columnspan=1, padx=10, pady=5, sticky='w')  # 上一步按钮
        tk.Button(self, font=ft1, text='下一步', command=self.next_photo).grid(
            row=2, column=1, columnspan=1, padx=10, pady=5, sticky='w')  # 下一步按钮
        tk.Button(self, font=ft1, text='显示', command=self.show_photo).grid(
            row=2, column=2, columnspan=1, padx=10, pady=5, sticky='w')  # 显示当前正在处理的图片
        tk.Button(self, font=ft1, text='暂存', command=self.save_photo).grid(
            row=2, column=3, columnspan=1, padx=10, pady=5, sticky='w')  # 暂存当前正在处理的图片
        tk.Button(self, font=ft1, text='保存到', command=self.save_photo_to).grid(
            row=3, column=3, columnspan=1, padx=10, pady=5, sticky='w')  # 保存图片到指定路径
        tk.Button(self, font=ft1, text='图形绘制', command=self.draw_frame).grid(
            row=4, column=0, columnspan=1, padx=10, pady=5, sticky='w')  # 保存图片到指定路径

    @update_photo('添加')
    def photo_file(self):
        """选择图片文件操作"""
        photo_path = tk.filedialog.askopenfilename(title='选择一张图片',
                                                   initialdir=(os.path.expanduser('F:\projects\PythonProject\Gui_cv2')))
        self.label["text"] = '路径:', photo_path  # 直接使用赋值的方法来修改
        end = '(gif|jpeg|jpg|png|pdf)'
        regex = '[C-F]:/(\w+\s*\w+/)+\w+\s*\w+\.' + end  # 提取路径,\s表示空格字符
        regex2 = '\w+\s*\w+\.' + end
        m = re.search(regex, photo_path)
        try:
            if m:
                self.photoId = 0
                self.img = cv2.imread(m.group(0))
                self.fileName = re.search(regex2, photo_path).group(0)  # 文件名
                self.present_photo = self.img.copy()
                self.imgList = []  # 操作列表清空
                self.imgList.append((self.img, '添加'))
                self.photo_flag = False
                self.present_action = '添加'
                self.name["text"] = self.fileName
                self.size["text"] = str(self.img.shape)
                self.last["text"] = '添加'
                img = cv2.resize(self.img, (500, 300), interpolation=cv2.INTER_NEAREST)  # 最近邻插值
                cv2.imshow('img', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                showinfo("info", '未找到图片，请重试')
        except Exception as e:
            showerror('Error', str(e))

    def last_photo(self):
        """上一张图片"""
        if self.photoId == 0:
            showwarning('Warning', "这已经是最早的图片了，不能再往前了！")
            return
        if self.photo_flag:
            message = askokcancel('提示！', '你当前有未保存的图片，是否保存？')
            if message:
                self.save_photo()
            else:
                self.present_photo = self.img.copy()
            self.photo_flag = False
        else:
            self.photoId -= 1
            self.img, self.last["text"] = self.imgList[self.photoId]
            self.size["text"] = self.img.shape
        img = cv2.resize(self.img, (500, 300), interpolation=cv2.INTER_NEAREST)  # 最近邻插值
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def next_photo(self):
        """下一张图片"""
        if self.photoId == len(self.imgList) - 1:
            showwarning('Warning', "这已经是最新的图片了，不能再往后了！")
            return
        if self.photo_flag:
            message = askokcancel('提示！', '你当前有未暂存的图片，是否保存？')
            if message:
                self.save_photo()
            self.photo_flag = False
        else:
            self.photoId += 1
            self.img, self.last["text"] = self.imgList[self.photoId]
            self.size["text"] = self.img.shape
        image = cv2.resize(self.img, (500, 300), interpolation=cv2.INTER_NEAREST)  # 最近邻插值
        cv2.imshow('img', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_photo(self):
        """保存当前修改的图片"""
        if not self.photo_flag:
            showinfo('info', '并没有更新的修改对象')
        else:
            self.photoId += 1
            self.imgList.append((self.present_photo, self.present_action))
            self.img, self.last["text"] = self.imgList[self.photoId]
            self.photo_flag = False

    def save_photo_to(self):
        """保存图片到指定路径"""
        file_path = tk.filedialog.askdirectory(title='选择保存目录',
                                               initialdir=(os.path.expanduser('F:\projects\PythonProject\Gui_cv2')))
        try:
            if os.path.isdir(file_path):  # 函数用于判断对象是否是一个目录
                print(file_path + self.fileName)
                cv2.imwrite('new' + self.fileName, self.present_photo)  # cv2只能保存到当前文件目录下，需要转移（前面加new避免重名及误删）
                shutil.move('new' + self.fileName,
                            os.path.join(file_path, self.fileName))  # os.path.join()函数用于路径拼接文件路径，可以传入多个路径
                showinfo('保存成功', '保存成功！')
            else:
                showwarning('warning', '请选择一个目录')
        except Exception as e:
            showerror('error', e)

    def show_photo(self):
        """原尺寸显示当前图片"""
        print(self.__repr__())
        cv2.imshow('img', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @update_photo('绘制')
    def draw_frame(self):
        """绘图窗口(应该单独设计成一个类的，大意了，懒得改了)"""
        # 基础设置
        image = self.present_photo # 以目前正在修改的图片作为原图
        dra = draw_cv(image) # 导入绘图类

        # 顶级窗口
        drawTop = tk.Toplevel()
        drawTop.attributes("-toolwindow", 1)
        drawTop.wm_attributes("-topmost", 1) # 置顶
        drawTop.title("作图窗口")
        drawTop.geometry("500x360")
        drawTop["bg"] = 'Silver'
        ft1 = tkFont.Font(size=15, slant=tkFont.ITALIC)
        color = (0, 0, 0) # 默认绘制颜色
        options = {0: '直线', 1: '矩形', 2: '圆圈', 3: '椭圆', 4: '多边形', 5: '文本'}
        option = options[0]  # 默认操作
        # 标签
        show = tk.Label(drawTop, text='当前操作:直线', font=ft1, bg='Silver')
        show.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        def draw_operation(n):
            """事件函数"""
            nonlocal option, options, actions
            option = options[n]
            show["text"] = '当前操作:' + options[n] + "  " + "当前颜色(bgr):" + str(color)
            actions[n]()

        def color_choose():
            """颜色函数"""
            nonlocal color, image
            color = dra.color_palette()
            show["text"] = '当前操作:' + option + "  " + "当前颜色:" + str(color)

        def check_pos():
            """查看当前剩余坐标点"""
            showinfo('coordinates:', str(dra.pointers))

        def synchronization():
            """同步图片"""
            self.present_photo = dra.img
            self.save_photo()
            dra.pointers.clear()

        def on_closing():
            """结束函数"""
            cv2.destroyAllWindows()
            drawTop.destroy()

        drawTop.protocol("WM_DELETE_WINDOW", on_closing)  # 窗口关闭事件
        # 绘图操作
        tk.Button(drawTop, font=ft1, text='画直线', command=lambda: draw_operation(0),  bg='Silver').grid(
            row=1, column=0, columnspan=1, padx=10, pady=5, sticky='w')
        tk.Button(drawTop, font=ft1, text='画矩形', command=lambda: draw_operation(1), bg='Silver').grid(
            row=1, column=1, columnspan=1, padx=10, pady=5, sticky='w')
        tk.Button(drawTop, font=ft1, text='画圆圈', command=lambda: draw_operation(2), bg='Silver').grid(
            row=1, column=2, columnspan=1, padx=10, pady=5, sticky='w')
        tk.Button(drawTop, font=ft1, text='画椭圆', command=lambda: draw_operation(3), bg='Silver').grid(
            row=2, column=0, columnspan=1, padx=10, pady=5, sticky='w')
        tk.Button(drawTop, font=ft1, text='画多边形', command=lambda: draw_operation(4), bg='Silver').grid(
            row=2, column=1, columnspan=1, padx=10, pady=5, sticky='w')
        tk.Button(drawTop, font=ft1, text='添加文本', command=lambda: draw_operation(5), bg='Silver').grid(
            row=2, column=2, columnspan=1, padx=10, pady=5, sticky='w')
        tk.Label(drawTop, text='参数修改:', font=ft1, bg='Silver').grid(
            row=3, column=0, columnspan=2, padx=10, sticky='w')
        tk.Label(drawTop, text='点击键盘Esc结束相应选择', font=ft1, bg='Silver').grid(
            row=3, column=1, columnspan=3, padx=10, sticky='w')
        tk.Button(drawTop, font=ft1, text='选择颜色', command=color_choose, bg='Silver').grid(
            row=4, column=0, columnspan=1, padx=10, sticky='w')
        tk.Button(drawTop, font=ft1, text='鼠标选取坐标', command=dra.add_points, bg='Silver').grid(
            row=4, column=1, columnspan=2, padx=10, sticky='w')
        # 粗细设置
        tk.Label(drawTop, text='粗细s:', font=ft1, bg='Silver', width=8).grid(
            row=5, column=0, columnspan=1, padx=10, sticky='w')
        thick = tk.StringVar()
        thick.set('3')
        tk.Entry(drawTop, textvariable=thick, font=ft1, bg='Silver', width=5).grid(
            row=5, column=1, columnspan=1, padx=10, sticky='w')
        # 半径设置
        tk.Label(drawTop, text='半径r:', font=ft1, bg='Silver', width=8).grid(
            row=5, column=2, columnspan=1, padx=10, sticky='w')
        radius = tk.StringVar()
        radius.set('10')
        tk.Entry(drawTop, textvariable=radius, font=ft1, bg='Silver', width=5).grid(
            row=5, column=3, columnspan=1, padx=10, sticky='w')
        # 长轴设置
        tk.Label(drawTop, text='长轴:', font=ft1, bg='Silver', width=8).grid(
            row=6, column=0, columnspan=1, padx=10, sticky='w')
        long_axis = tk.StringVar()
        long_axis.set('10')
        tk.Entry(drawTop, textvariable=long_axis, font=ft1, bg='Silver', width=5).grid(
            row=6, column=1, columnspan=1, padx=10, sticky='w')
        # 短轴设置
        tk.Label(drawTop, text='短轴:', font=ft1, bg='Silver', width=8).grid(
            row=6, column=2, columnspan=1, padx=10, sticky='w')
        short_axis = tk.StringVar()
        short_axis.set('5')
        tk.Entry(drawTop, textvariable=short_axis, font=ft1, bg='Silver', width=5).grid(
            row=6, column=3, columnspan=1, padx=10, sticky='w')
        # 角度设置
        tk.Label(drawTop, text='angle:', font=ft1, bg='Silver', width=8).grid(
            row=7, column=0, columnspan=1, padx=10, sticky='w')
        angle = tk.StringVar()
        angle.set('0')
        tk.Entry(drawTop, textvariable=angle, font=ft1, bg='Silver', width=5).grid(
            row=7, column=1, columnspan=1, padx=10, sticky='w')
        # 文字大小设置
        tk.Label(drawTop, text='文字大小:', font=ft1, bg='Silver', width=8).grid(
            row=7, column=2, columnspan=1, padx=10, sticky='w')
        size = tk.StringVar()
        size.set('4')
        tk.Entry(drawTop, textvariable=size, font=ft1, bg='Silver', width=5).grid(
            row=7, column=3, columnspan=1, padx=10, sticky='w')
        # 起始角设置
        tk.Label(drawTop, text='sAngle:', font=ft1, bg='Silver', width=8).grid(
            row=8, column=0, columnspan=1, padx=10, sticky='w')
        sAngle = tk.StringVar()
        sAngle.set('0')
        tk.Entry(drawTop, textvariable=sAngle, font=ft1, bg='Silver', width=5).grid(
            row=8, column=1, columnspan=1, padx=10, sticky='w')
        # 终点角设置
        tk.Label(drawTop, text='eAngle:', font=ft1, bg='Silver', width=8).grid(
            row=8, column=2, columnspan=1, padx=10, sticky='w')
        eAngle = tk.StringVar()
        eAngle.set('360')
        tk.Entry(drawTop, textvariable=eAngle, font=ft1, bg='Silver', width=5).grid(
            row=8, column=3, columnspan=1, padx=10, sticky='w')
        # 文本设置
        tk.Label(drawTop, text='Text:', font=ft1, bg='Silver', width=8).grid(
            row=9, column=0, columnspan=1, padx=10, sticky='w')
        text = tk.StringVar()
        text.set('cv2')
        tk.Entry(drawTop, textvariable=text, font=ft1, bg='Silver', width=20).grid(
            row=9, column=1, columnspan=3, padx=10, sticky='w')
        # 查看当前选取的坐标点
        tk.Button(drawTop, font=ft1, text='查看选取的坐标', command=check_pos, bg='Silver').grid(
            row=10, column=0, columnspan=2, padx=10, sticky='w')
        # 同步图片并清空坐标列表
        tk.Button(drawTop, font=ft1, text='同步并清空', command=synchronization, bg='Silver').grid(
            row=10, column=2, columnspan=2, padx=10, sticky='w')

        def line():
            """绘制直线"""
            nonlocal thick
            if len(dra.pointers) < 2:
                showinfo('info', '请先选取直线起始坐标')
                return
            else:
                start = dra.pointers.pop(0)
                end = dra.pointers.pop(0)
                dra.draw_line(start, end, int(thick.get()))

        def rectangle():
            """绘制矩形"""
            nonlocal thick
            if len(dra.pointers) < 2:
                showinfo('info', '请先选取矩形的左上角和右下角坐标')
                return
            else:
                lft = dra.pointers[0]
                rit = dra.pointers[1]
                dra.pointers = dra.pointers[2:]
                dra.draw_rectangle(lft, rit, int(thick.get()))

        def circle():
            """绘制圆圈"""
            nonlocal radius, thick
            if len(dra.pointers) < 1:
                showinfo('info', '请先选取圆的中心坐标')
                return
            else:
                center = dra.pointers.pop(0)
                dra.draw_circle(center, int(radius.get()), int(thick.get()))

        def ellipse():
            """画椭圆"""
            nonlocal thick, long_axis, short_axis, angle, sAngle, eAngle
            if len(dra.pointers) < 1:
                showinfo('info', '请先选取椭圆的中心坐标')
                return
            else:
                center = dra.pointers.pop(0)
                dra.draw_ellipse(center, (int(long_axis.get()), int(short_axis.get())), float(angle.get()),
                                 float(sAngle.get()), float(eAngle.get()), int(thick.get()))

        def polylines():
            """绘制多边形"""
            nonlocal thick
            if len(dra.pointers) < 2:
                showinfo('info', '请先选取多边形各顶点坐标')
                return
            else:
                dra.draw_polylines([dra.pointers], True, int(thick.get()))
                dra.pointers.clear()

        def putText():
            """添加文本"""
            nonlocal text, thick
            if len(dra.pointers) < 1:
                showinfo('info', '请先选取添加文本的位置坐标')
                return
            else:
                lft = dra.pointers.pop(0)
                dra.draw_Text(text.get(), lft, int(size.get()), int(thick.get()))

        # 函数事件列表
        actions = [line, rectangle, circle, ellipse, polylines, putText]


if __name__ == '__main__':
    root = MyTk()
    tk.mainloop()
