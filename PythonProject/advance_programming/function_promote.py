"""函数式编程"""
# 高阶函数：可将函数名作为变量表示, 传递和返回值
x = abs(-5)
print(x)
x = abs
print(x(-5))

def add(x1, x2, f):
    return f(x1) + f(x2)

print(add(-5, 6, abs))
# 内置高阶函数:map(), reduce()

# 函数的惰性计算：实现一种延迟性的计算，使得函数的计算并非是在函数返回的时候执行，而通过一定控制来人为决定函数的执行时间，如生成器和迭代器
# 函数的闭包:一个函数内部又定义了另一个函数，这种结构称为函数的闭包。外部函数称为外函数，内部函数称为内函数。使用关键字：nonlocal
def lazy_sum(*args):
    s = 0
    def get_sum():
        nonlocal s
        for n in args:
            s = s + n
        return s
    return get_sum

list1 = list(range(5))
f1 = lazy_sum(*list1)
print(f1)
print(f1())
print(f1()) # 会将s值保留

# 装饰器：建立一个以装饰器名称命名的函数闭包，在闭包内添加该装饰器所需要的程序逻辑，当Python解释器执行到@log装饰器时，会自动调用装饰器名所对一个的函数，并作为参数传入
# 若有多个装饰器，会先按顺序执行其外函数，然后在按顺序执行内函数
def log(func):
    def inner():
        print('function logged')
        func()
    return inner

@log
def f1():
    print("f1 worked")
f1()
# 装饰带参数的函数
def wing(func):
    def inner(name):
        print(name + 'has wings')
        func(name)
    return inner
@wing
def fly(name):
    print(name + 'can fly')
fly('Bird')
# 带参数的装饰器:再原有基础上增加一层闭包(类函数装饰器要写在类外面)
def log(arg='sys'): # 装饰器的输入参数
    def outer(func): # 外函数
        def inner(): # 内函数
            print('function logged for %s' % arg) # 模拟添加日志
            func()
        return inner # 外函数的返回值为内函数名称
    return outer # 日志闭包的返回值
@log('app')
def f1():
    print('f1 worked')
f1()
# 通用装饰器:在实际应用中，为不同输入参数选择一种较为通用的装饰器，统一处理——将内函数的参数部分设置为*args和**kwargs
def my_decorator(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(args)
        print(kwargs)
        return ret
    return inner
@ my_decorator
def test1():
    print('test1 called')
test1()

# 类函数装饰器要写在类外面
def update_photo(func):
    """用于加入每个图像处理按钮的装饰器"""

    def inner(self, *args, **kwargs):
        self.photo_flag = True
        self.present_photo = self.imgList[self.photoId]
        print('图片参与修改')
        func(self, *args, **kwargs)

    return inner

# 偏函数：见前面