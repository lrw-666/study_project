"""GUI编程"""
# 主要使用Python默认GUI库TK
import tkinter

# GUI程序启动可运行的5个主要步骤：
# 1.导入Tkinter模块 2.创建一个顶层窗口对象，用于容纳GUI应用 3.在顶层窗口对象之上构建所有的GUI组件(及其功能) 4.通过底层的应用代码将这些GUI组件连接起来 5.进入主事件循环

# 顶层窗口对象：GUI对象可以有多个顶层窗口，但其中只能有一个是根窗口
# top = tkinter.Tk() # 返回根窗口
# 控件包含其他控件，就可以将其认为是那些控件的父控件

# 事件驱动处理
# 布局管理器:创建所有的GUI组件，然后将他们绘制在屏幕上。
# 然后GUI进入其类似服务器的无限循环，知道GUI事件，处理，在等待更多事件 mainloop()函数一般为最后一段代码

# 布局管理器：TK有三种布局管理器帮助控件集进行定位
# Placer：你提供控件的大小和摆放位置，然后管理器就会将其摆放好
# Packer：把控件填充到正确的位置(指定父控件中)，然后对于之后的每个控件，回去寻找剩余的空间进行填充
# Grid：基于网格坐标来指定GUI控件的放置

# Packer没有收到其他指示时，所有控件都是垂直排列的，若想要水平布局需要创建一个新的Frame对象来添加按钮
# 实例：
def text1():
    top = tkinter.Tk()
    label = tkinter.Label(top, text='Hello World!')
    label.pack() # 让Packer来管理和显示控件

    quit = tkinter.Button(top, text='Quit', command=top.quit, bg='red', fg='white') # 安装一个回调函数，当按钮按下并释放后整个程序就会退出
    quit.pack(fill=tkinter.X, expand=1)

    tkinter.mainloop() # 运行

label = None
scale = None
def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

def text2():
    global label
    global scale
    top = tkinter.Tk()
    top.resizable(0, 0)# 禁止调整宽高
    top.geometry("250x150") # 注意中间是个x符号，是该函数的参数风格，还有+-，若为None则获取此时窗口的宽高及位置

    label = tkinter.Label(top, text='Hello World', font='Helvetica -12 bold')
    label.pack(fill=tkinter.Y, expand=1)
    scale = tkinter.Scale(top, from_=10, to=40, orient=tkinter.HORIZONTAL, command=resize) # resize为回调函数，当滑块移动时被激活
    scale.set(12) # 初始值为12
    scale.pack(fill=tkinter.X, expand=1)

    quit = tkinter.Button(top, text='Quit', command=top.quit, activeforeground='white', activebackground='red')  # 安装一个回调函数，当按钮按下并释放后整个程序就会退出
    quit.pack()

    tkinter.mainloop()

# 偏函数(PFA)：函数式编程，可通过有效地冻结那些预先确定的参数来缓存函数参数，然后在运行时，当获得需要的剩余参数后，可以将它们冻结，传递到最终的参数中，从而使最终确定的所有参数去调用函数
# 偏函数可以用于可调用对象(任何包括函数接口)，只需要通过使用圆括号即可，包括类、方法或可调用实例
# GUI编程是一个很好的偏函数用例，用于参数类似的对象
from functools import partial as pto
from tkinter.messagebox import showinfo, showwarning, showerror
# functools 模块可以说主要是为函数式编程而设计，用于增强函数功能。用以为可调用对象（callable objects）定义高阶函数或操作。
# from tkMessageBox import showinfo, showwarning, showeror 在python3.4中，原来的tkMessageBox变成tkinter.messagebox
# Tkinter tkMessageBox: tkMessageBox模块用于显示在您的应用程序的消息框。此模块提供了一个功能，您可以用它来显示适当的消息
WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'
SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging, traffic': WARN,
    'one way': REGU
}
critCB = lambda: showerror('Error', 'Error Button Pressed')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('info', 'Info Button Pressed!')
# lambda作为一个表达式，定义了一个匿名函数，如：g = lambda x:x+1， 代码x为入口参数，x+1为函数体 g(1)==2
def text_pfa():
    top = tkinter.Tk()
    top.title('Road Signs')
    tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

    MyButton = pto(tkinter.Button, top) # partial用于创建一个偏函数，将默认参数包装一个可调用对象，返回结果也是可调用对象。偏函数可以固定住原函数的部分参数，从而在调用时更简单。
    CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
    WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
    ReguButton = pto(MyButton, command=infoCB, bg='white')

    for eachSign in SIGNS:
        signType = SIGNS[eachSign]
        # %是格式符号，%d代表整数，%s代表字符 中间的%代表用它后面的参数代替前面的%s
        cmd = '%sButton(text=%r%s).pack(fill=tkinter.X, expand=True)' % (
            signType.title(), eachSign,
            '.upper()' if signType == CRIT else '.title()') # 此处为一个三元/条件操作符
        eval(cmd) # eval() 函数用来执行一个字符串表达式，并返回表达式的值,此处用来实例化按钮
    top.mainloop()

# 更多：Label(top, text=''), Frame(top), Scrollbar(Frame), Listbox(Frame, height, width, yscrollcommand=Scrollbar.yview)
# Listbox（列表框）组件用于显示一个选择列表。Listbox 只能包含文本项目，并且所有的项目都需要使用相同的字体和颜色。根据组件的配置，用户可以从列表中选择一个或多个选项。
# Entry(top, width, textvariable):文本框用来让用户输入一行文本字符串
# StringVar(top), 在Python中，StringVar是可变字符串，get()和set()是得到和设置其内容
# os.getcwd()与os.curdir都是用于获取当前执行python文件的文件夹，不过当直接使用os.curdir时会返回‘.’(这个表示当前路径），记住返回的是当前执行python文件的文件夹，而不是python文件所在的文件夹。
# os.path.exists() os.path.isdir()
# bind()方法：绑定意味着将一个回调函数与按键、鼠标操作或一些其他事件连接起来，当用户发起这类事件时，回调函数就会执行

# 其他GUI：Tix(TK接口扩展)、pmw、wxPython、PyGTK
# 扩展控件(Tix)：Control(即SpinButton):由一个文本控件和一组靠近的箭头按钮组成，文本控件中的值可被附近的一组箭头按钮"控制"或”上下调整“， ComboBox：下拉框 模块Tix
# top.eval是Tk对象的一个特殊函数。 用于检查包的版本号。 ‘package require Tix'这一句话是TCL语言的语法。因为Tkinter本身就是TCL的库，只是被python拿来用。top.tk.eval('package require Tix')会断言应用中Tix模块是可用的
# PMW：解决Tkinter的老旧问题，添加了一些更新式的控件 Counter：提供了验证输入数据的方法， 模块Pmw
# wxWidgets和wxPython：C++实现，有Python和Perl接口一个可以构建图形用户应用的跨平台工具包，使用了每个平台上的原生GUI， 模块wx
# wx.Frame(), wx.BoxSizer(), wx.Font(), wx.StaticText(), wx.SpinCtrl(),
# GTK+和PyGTK：与上者类似 模块pygtk，gtk， pango(一个用于文本布局和渲染的库，是GTK+中文本和字体处理的核心)

# Tile\Ttk:重新实现了大多数TK核心控件，添加了很多新控件，引入了主题引擎，与TK8.5的核心结合为Ttk，用于辅助Tk控件集，3.1版本后，可通过tkinter.ttk导入

if __name__ == '__main__':
    # text2()
    text_pfa()