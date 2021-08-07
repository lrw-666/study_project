import tkinter as tk
import tkinter.filedialog
import tkinter.font as tkFont
from tkinter.messagebox import showinfo, showwarning, showerror, askokcancel
import os
import re
from functools import partial as pto
import cv2
import shutil

"""用户的可视化界面"""


# 类函数装饰器要写在类外面
def update_photo(action='添加'):
    """用于加入每个图像处理按钮的装饰器（带操作参数）"""

    def outer(func):
        def inner(self, *args, **kwargs):
            self.photo_flag = True
            self.present_photo = self.imgList[self.photoId]
            self.present_action = action
            self.last["text"] = action
            print('图片操作:', self.present_action)
            func(self, *args, **kwargs)

        return inner

    return outer


# 定义主框架
class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('图像处理')  # 框名
        self.resizable(1, 0)  # 框体大小可调，分别为x，y方向的可变性
        self.geometry('450x550')  # 主框体大小
        self.fileName = '001.jpg'  # 图片文件名
        self.img = cv2.imread(self.fileName)  # 设置默认图片(此时正在处理的图像)
        self.imgList = [(self.img, '添加'), ]  # 初始化图片列表
        self.photoId = 0  # 记录当前显示图片
        self.photo_flag = False  # true表示存在正在处理中的图片（未保存）
        self.present_photo = self.img  # 当前正在处理的图片
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
        return "%s \n当前图片名:%s \n当前图片大小:%s \n进行的操作:%s" % (self.__class__.__name__, self.fileName, str(self.img.shape), actions)

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
                self.present_photo = self.img
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
            self.photo_flag = False
        else:
            self.photoId -= 1
            self.img, self.last["text"] = self.imgList[self.photoId]
            self.size["text"] = self.img.shape
        img = cv2.resize(self.img, (500, 300), interpolation=cv2.INTER_NEAREST)  # 最近邻插值
        cv2.imshow('img1', img)
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
        img = cv2.resize(self.img, (500, 300), interpolation=cv2.INTER_NEAREST)  # 最近邻插值
        cv2.imshow('img2', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_photo(self):
        """保存当前修改的图片"""
        if self.photo_flag:
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

    @update_photo('删除')
    def show_photo(self):
        """原尺寸显示当前图片"""
        print(self.__repr__())
        cv2.imshow('img', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    root = MyTk()
    tk.mainloop()
