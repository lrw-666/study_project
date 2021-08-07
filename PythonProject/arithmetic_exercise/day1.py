# 对于一个大小为n的list来说，调用一次append的复杂度是O(1),而调用一次insert（插入位置是0）的复杂度则为O(n)
# list类型实际上是一个动态数组，优势在是一个被调试好了的，速度很快的数据结构，胜过我们用纯python环境实现的列表结构
# 一般整数与大整数的时间效率是有区别的
# timeit模块:为指向相对可靠的计时操作而设计的(通过多次运行相关代码的方式来提高计时精度，要避免一些因重复执行带来的副作用)
import timeit

print(timeit.timeit("x = 2 + 2"))
# cProfile模块:给出关于执行时间都花在哪里的更为详细的信息
import cProfile


def sum_1():
    s = 0
    for i in range(10):
        s += i
    print(s)


print(cProfile.run('sum_1()'))
# 对自己针对某概要问题实例提出的算法进行实证研究——trace模块:对程序中个语句的执行次数进行计数操作
# 通过Python Call Graph工具：可视化看到代码的调用情况

# 散列：用值来索引数组元素，Python语言中，标准散列机制由hash函数提供，调用一个对象的__hash__方法，机制常用于字典类型(dict)、集合类型(set)
# hash方法是用来构建哈希表的，其他哈希，有一个标准库hashlib模块

""" 图 """
# 邻接列表及其类似结构:针对每对节点设置一个邻居列表（列表或set等容器类型)
# {c}表示set类型，字面写法set([1, 2, 3]), 可用{1,2, 3}表示，但主要{}表示空dict，空set写法为set()
# 列表可重复有序、集合不可重复无序
# 邻接集(有向)写法:
a, b, c, d, e, f, g, h = range(8)
N = [  # N[v]为v的邻居节点集
    {b, c, d, e, f},  # a的连接点
    {c, e},  # b
    {d},  # c
    {e},  # d
    {f},  # e
    {c, g, h},  # f
    {f, h},  # g
    {f, g}  # h
]  # 将里面集合用列表来表示即为邻接列表
# 邻居检测
print(b in N[a])  # 列表表示的话，操作一样，但成员检测变成了O(n)级操作，速度放缓
# 长度
print(len(N[f]))
# 邻接列表(或数组)可让我们在维持低成本的情况下，对N(v)中所有节点v进行有效遍历(可二分优化)，然而邻居检测的成本很高。若图的结构很密集，选择邻接集
# 删除一个位于list中间的对象操作成本很高，而从尾部删除只需要常数时间。
# 若不在乎邻居节点顺序的话，可用当前邻接列表中最后一项覆盖需要删除的邻居节点(常数时间)，然后调用pop方法

# 用dict类型来替代set或list，附加权重
# 加权邻接字典
N = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},  # a的连接点
    {c: 4, e: 3},  # b
    {d: 8},  # c
    {e: 7},  # d
    {f: 5},  # e
    {c: 2, g: 2, h: 2},  # f
    {f: 1, h: 6},  # g
    {f: 9, g: 8}  # h
]
print(b in N[a])
print(len(N[f]))
print(N[a][b])
# 若需要的话，可使用邻接字典来表示没有加权边的情况，也可以用邻接字典表示(相关值用None或占位符替代)，这样能发挥出邻接集合的优势

# 使用dict类型来充当主要结构是更好的选择
# 邻接集的字典表示法：
N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('f')
}# 省略set构造器，最终得到的是一个邻接字符串(不可变的字符类的邻接列表)

# 邻接矩阵:不再列出每个节点的所有邻居节点，而是将每个节点可能的邻居位置排成一行(数组)，
# 然后用某个值(True,False)来表示相关节点是否为当前节点的邻居
# 用嵌套list实现的邻接矩阵
a, b, c, d, e, f, g, h = range(8)
N = [[0, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 1, 1, 1, 1, 1, 1],
     [0, 1, 0, 1, 1, 1, 1, 1],
     [0, 1, 1, 0, 1, 1, 1, 1],
     [0, 1, 1, 1, 0, 1, 1, 1],
     [0, 1, 1, 1, 1, 0, 1, 1],
     [0, 1, 1, 1, 1, 1, 0, 1],
     [0, 1, 1, 1, 1, 1, 1, 0]] # 也可用true或false来表示
# 邻接检测：
print(N[a][b])
# 节点的邻居数:
print(sum(N[f]))
# 邻接矩阵特性：
# 1.避免自循环,对角线上的值应全为假
# 2.无向图的邻接矩阵应该是一个对称矩阵
# 3.将邻接矩阵扩展成允许对边进行加权处理：在原来的存储真值的地方直接存储相关的权值即可
# 4.通常将不存在的边权值设置为无穷大或非法权值(如None, -1(无负数的情况))
# 整型加权值：sys.maxint 浮点型表示无穷大的值:inf,可通过float('inf')来获取它

# 对不存在的边赋予无限大权值的加权矩阵
inf = float('inf')
W = [[0, 2, 1, 3, 8, 7, inf, inf],
     [inf, 0, 4, inf, 3, inf, inf, inf], # 下面类似就行
     [0, 1, 0, 1, 1, 1, 1, 1],
     [0, 1, 1, 0, 1, 1, 1, 1],
     [0, 1, 1, 1, 0, 1, 1, 1],
     [0, 1, 1, 1, 1, 0, 1, 1],
     [0, 1, 1, 1, 1, 1, 0, 1],
     [0, 1, 1, 1, 1, 1, 1, 0]]
# 成员检测：
print(W[a][b] < inf)
# 邻居数检测
print(sum(1 for w in W[a] if w < inf) - 1) # 减去对角线

# 最后:根据图的具体用处来选择相关的表示法

# Numpy库中的专用数组
import numpy as np
# 基于list的空加权矩阵
N = [[0]*10 for i in range(10)]
# 基于Numpy
N = np.zeros([10, 10])
print(N[1, 1]) # 内部元素可通过一对由逗号分割的索引值来访问
print(N[1]) # 给定节点的邻居列表

# 若处理的相对稀疏的图，可通过稀疏矩阵的形式来节省内存 如scipy.sparse模块

""" 树 """
# 图的特殊情况，可用图的方法来表示树
# 带根的树结构：层次结构，根节点代表全部对象
# 二维列表表示树：
T = [["a", "b"], ["c"], ["d", ["e", "f"]]]
print(T[0][1])
print(T[2][1][0])
# 二叉树:各节点最多拥有两个子节点
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

t = Tree(Tree("a", "b"), Tree("c", "d"))
print(t.right.left)
# 可用None来表示不存在的子节点

# 多路搜索树:先子节点，后兄弟节点
class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids # val为相关的值提供一个更具描述性的名称
        self.next = next

t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
print(t.val)
print(t.kids.next.next.val)

# Bunch模式:当树这样的数据结构被原型化(或被定型)时,一种允许我们再起构造器中设置任何属性的灵活的类型，有多种实现方式
# 主要要素:
class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self
# class 通过内置成员_ dict _ 存储成员信息包括自己（_ dict _ 字典）通过dir函数可以查看该dict，
# 当类实例成员属性发生变动时，会调用 _ setattr _ ，在这个方法下必须进行对属性的赋值操作 self._ dict_ [name] = value

# 此模式能让我们以命令行参数形式创建相关对象，并设置任意属性
x = Bunch(name="Jayne Cobb", position="Public Relations")
print(x.name)
# 继承dict类，获得大量相关内容
T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
print(t.left.right)
print(t['left']['right'])
print("left" in t.right)

# 多种表示法:
# 图：边列表、边集、关联矩阵等等
# 子问题图：绝大部分问题应该都可以被分为若干个子问题，这些子问题在结构上往往非常相似
# 因此，这些结可被看作相关子问题图中的节点，而之间的依赖关系为该图的边
# 提供非常重要的分析：分治法、动态规划等等

# 图结构库：NetworkX、python-graph、Graphine、Graph-tool

"""性能陷阱"""
# 当性能成为重点问题是，要着重实际分析而不是直觉。
# 当正确性至关重要时，最好用不同的实现题来对答案进行多次计算

# 小心黑盒子（不是自己写的组件）,有陷阱
# 隐藏的性能陷阱(可能将一个线性级操作变为平方级操作)：隐性平方级操作
# 两种查询列表方式
from random import randrange
L = [randrange(10000) for i in range(1000)] # 返回指定递增基数集合中的一个随机数
print(42 in L)
S = set(L)
print(42 in S)
# 成员查询在list中是线性级的，在set中是常数级的。
# 依次往某个集合里添加新值，并在每一步检查该值是否已被添加：list处理为平方级，而set为线性级

# 例1
# S = ""
# for chunk in string_producer():
#     s += chunk
# 字符串的多次修改:在扩展到某一规模前都很好，但随后这些优化的作用就会消退
# 问题：每次执行+=操作时新建一个字符串，并复制上一个字符串(排除优化)
# append操作允许将原有空间加上一定百分比来进行“过度”分配，可用空间的增长方式是指数式的。
# 这时append操作的成本在交由所有操作平均承担的情况就成了常数级操作
# 优化：
# chunks = []
# for chunk in string_producer():
#     chunks.append(chunk)
# s = ''.join(chunks)
# 再简化：
# S = ''.join(string_producer)

# 例2
lists = [[1, 2], [3, 4, 5], [6]]
sum(lists, []) # 平方级
# 优化
res = []
for lst in lists:
    res.extend(lst)

# 浮点运算的麻烦:浮点数天然是不准确的
print(sum(0.1 for i in range(10)) == 10) # False
# 不要对浮点数进行等值比较，检查它们是否接近与相等——unittest模块的assertAlmostEqual方法类似思路
def almost_eaual(x, y, places=7):
    return round(abs(x-y), places) == 0

print(almost_eaual(sum(0.1 for i in range(10)), 1.0))
# 如果需要某种精确的十进制浮点数表示法——decimal模块
from decimal import *
print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
# 在某些特定数学以及科学应用中——Sage模块（Sage使用的是数学上的语义符号）
