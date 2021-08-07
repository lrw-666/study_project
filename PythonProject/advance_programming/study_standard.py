import pprint
import sys

"""Python 标准库"""
# 告诉解释器去哪里找这个模块:sys.path.append('C:/python') UNIX中，必须使用完整路径，自动创建完整路径——sys.path.expanduser('~/python)
# 导入模块时，其所在目录除源代码文件外，还新建了一个__pycache__的子目录，包含处理后的文件，Python能更高效的处理它们
# 模块只导入一次，避免循环导入，可使用importlib中的函数reload，重新导入模块
# 检查模块是否作为程序运行还是被导入另一个程序：使用变量__name__,在主程序中，变量__name__的值是'__main__'

# Python打包用户指南:packaging.python.org
# 让模块可用
# 1.将模块放在正确的位置：找出Python解释器到哪里去查找模块，再将文件放在这个地方。可在sys的变量path中找到目录列表
pprint.pprint(sys.path)
# 2.告诉解释器到哪里去查找：将模块所在的目录包含在环境变量PYTHONPATH中。还可使用路径配置文件，扩展名为.pth
# 环境变量是操作系统的一部分

# 包：模块存储在扩展名为.py的文件中，而包是一个目录，要被Python视为包，目录必须包含文件__init__.py，该文件内容就是包的内容。
# 要将模块加入包中，只需将模块文件放在包目录中即可，可嵌套包。导入包可使用文件__init__.py的内容，但不能使用其他模块，要单独导入

"""探索模块"""
# 模块包含什么：1.使用dir 2.变量__all__
# 使用函数dir，列出对象的所有属性，以下划线打头的名称不能为外部使用
import copy
print([n for n in dir(copy) if not n.startswith('_')])
# 变量__all__：包含一个模块内部设置的列表
print(copy.__all__) # 告诉你导入copy能用的

# 使用help：
print(help(copy))
print(help(copy.copy)) # 获取函数copy的信息
print(copy.copy.__doc__)
# __doc__字符串:在函数开头编写的字符串，用于对函数进行说明

# 文档：查看函数参数
print(range.__doc__)

# 使用源代码：
# 1.像解释器那样通过sys.path来查找 2.查看模块特性__file__
print(copy.__file__)

"""一些常用标准库"""
# sys:argv, exit, modules, path, platform, stdin, stdout, stderr
# 从命令行调用Python脚本时，可能需要指定一些脚本，这些参数将放在列表sys.argv中，其中sys.argv[0]为Python脚本名
import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

# os:访问多个操作系统服务 environ、system、sep、pathsep、linesep、urandom
# 访问环境变量
import os
print(os.environ['PYTHONPATH'])
# os.system用于运行外部程序，execv和popen分别用于退出Python解释器和创建一个到程序的连接，模块subprocess融合了这三个功能
# 模块webbrowser更佳用于启动web浏览器

# fileinput:迭代一系列文本文件的所有行 input, filename, lineno, filelineno, isfirstline, isstdin, nextfile, close

# 集合、堆和双端队列
# 集合:内置类set union,copy等等, 可变，但只包含不可变的值， frozenset类型表示不可变的集合(集合包含集合)
print(set(range(10))) # 花括号、顺序不定， 空花括号会被认为空字典
print(type({}))
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b)) # 并集
print(a & b) # |, >, <, =, +, -, ^,
# 堆:优先队列，以任意顺序添加对象，并随时找出最小的元素，效率高于min方法
# 堆操作函数的模块：heapq——heappush, heappop, heapify, heapreplace, nlargest, nsmallest  使用列表来表示堆对象本身
from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print(heap)
heappush(heap, 0.5)
print(heap) # 堆特性:位置i处的元素总是大于位置i//2处的元素
# 双端队列(及其他集合):模块collections， 包含类型deque以及其他几个集合类型
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
q.popleft() # 左弹出
print(q)
# time:获取当前时间、操作时间和日期、从字符串中读取日期、将日期格式化为字符串的函数，日期可表示为实数或包含9个整数的元组(年、月、日、时、分、秒、星期、儒略日、夏令时)
# asctime, localtime, mktime, sleep, strptime, time
import time
print(time.asctime()) # 将当前时间转换为字符串
# 模块datatime和timeit提供日期和时间算术支持，后者可帮助计算代码段的执行时间
# random：生成伪随机的函数 真正随机：os.urandom random.SystemRandom
# random, getrandbits, uniform, randrange, choice, shuffle, sample
# shelve和json:将数据存储到文件中
# shelve:open, close 像操作字典一样操作
import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c'] # shelf对象中的元素并非普通的映射关系：当你查看shelf对象中的元素是，将使用存储版重建该对象，而当你将一个元素赋给键时，该元素将被存储
s['x'].append('d')
print(s['x']) # 解决：使用临时变量或将open函数的参数writeback设置为True，这样从shelf对象读取或赋给它的所有数据结构都将保存到内存，并等到你关闭shelf对象时将其写入磁盘
# re:正则表达式
# argparse:提供功能齐备的命令行界面
# cmd:能够编写类似于Python交换式解释器的命令行解释器
# csv:CSV指逗号分隔的值
# datetime:时间跟踪需求
# difflib:确定两个序列的相似程度
# enum：枚举类型
# functools:让你能够在调用函数时只提供部分参数，以后再填充其他参数
# hashlib：计算字符串的小型签名数
# itertools：包含大量用于创建和合并迭代器的工具
# logging：日志
# timeit, profile和trace:测试代码段执行时间、用于对代码段的效率进行更全面的分析、进行覆盖率分析
# shutil：针对文件与文件夹各种操作