"""Microsoft Office 编程"""
# 利用Python进行COM客户端编程
# Windows编程：WindowsAPI、派生进、MFC GUI开发、Windows多线程编程、服务、远程访问、管道、服务器端COM编程以及事件

# 客户端COM编程
# 4个主流Office应用开发：Excel、Word、PowerPoint和Outlook

"""扩展Python"""
# 一般来说，任何可以集成或导入另一个Python脚本的代码都是一个扩展
# Python特性：无论是扩展还是普通Python模块，解释器与其交互方式完全相同

# UNIX系统编译c： gcc 文件名.c -o 文件名

# 开发者需要精心设计扩展代码，若需要与Python解释器交互，会用到一些格式固定的代码
# 样板代码主要含有四部分：
# 1.包含Python头文件： # include "Python.h"
# 2.为每一个模块函数添加形如PyObject* Module_func()的封装函数：对于每个需要在Python环境中访问的函数，需要创建一个以static PyObject*标识
# ，以模块名开头，紧接着是下划线和函数名本身的函数，可以import 文件名和 文件名.函数名()的形式在任意地方调用fac()函数(或from 文件名 import 函数名，直接函数名())
# 3.为模块编写PyMethodDef ModuleMethods[]数组任务：在某个地方将函数列出来，以便让Python解释器中的如何导入并访问这些函数
# 4. 添加模块初始化函数void initModule()
# 封装函数的任务是将Python中的值转成C形式，接着调用相应的函数，当c函数执行完毕时，需要返回Python的环境中.
# 封装函数需要将返回值转换成Python形式，并进行真正的返回，传回所有需要的值
# 如何转换：从Python到c时，调用一系列的PyArg_Parse*()函数，从c返回Python时，调用Py_BuildValue()函数

# 另一种创建扩展的方式是先编写封装代码，使用存根(stub)函数、测试函数或假函数，在开发工程中将其替换成具有完整功能的实现代码

# 编译阶段：为构建新的Python封装扩展，需要将其与Python库一同编译，现使用distutils包来编译
# 1. 创建setup.py文件 2.运行setup.py来编译并链接代码 3.在Python中导入模块 4.测试函数

# 引用计数：Python使用引用计数来追踪对象，并释放不再引用的对象，这是Python垃圾回收机制的一部分。创建扩展时也要注意如何处理Python对象
# 一个对象有两种类型的引用，一种是拥有引用，对该对象的引用计数递增1表示拥有该对象的所有权，用完后需要处理
# 还有一个借用引用：一般用于传递对象的引用，但不对数据进行任何处理。只要在其引用计数递减至零后就不继续使用这个引用，就无须担心其引用计数
# 可以通过一对C宏来改变Python对象的引用计数，Py_INCREF(obj):递增对象obj的引用计数 Py_DECREF(obj):递减对象obj的引用计数
# Py_INCREF(obj)和Py_DECREF(obj)还有一个先检测对象是否为NULL的版本，分别为Py_XINCREF()和Py_XDECREF()

# 线程和全局解释器锁：让扩展开发者释放GIL(全局解释器锁)
# 如在执行系统调用前就可以实现：通过将代码和线程隔离实现的，这些线程使用了另外的两个C宏：Py_BEGIN_ALLOW_THREADS和Py_END_ALLOW_THREADS，保证了运行和非运行时的安全性
# 用这些宏围起来的代码块会允许其他线程在其执行时同步执行

"""嵌入Python"""
# 用来编写扩展的工具：SWIG、Pyrex、Cython、Psyco、PyPy
# 嵌入是Python的另一项特性，在C应用中封装Python解释器