"""分解、合并、解决"""


# 树状问题即平衡问题
# 分治类算法三个概念性思维：分治递归法、强归纳法、递归遍历法
# 分治算法的工作过程：输入一个元素集合，将其对半分成两个规模大致相同的集合(最多线性操作),然后该算法会在这两半元素持续递归下去，并最终合并出结果（最多线性操作）

# 分治语义的一种通用性实现
def divide_and_conquer(S, divide, combine):
    if len(S) == 1:
        return S
    L, R = divide(S)
    A = divide_and_conquer(L, divide, combine)
    B = divide_and_conquer(R, divide, combine)
    return combine(A, B)  # 例如归并排序


# 折半搜索(二分法)：在一个有序序列上执行
# Python标准库中的bisect模块的bisect函数(bisect_right)和bisect_left函数,用C实现的
from bisect import bisect, bisect_left

a = [0, 2, 3, 5, 6, 8, 8, 9]
print(bisect(a, 5))
print(bisect_left(a, 5))


# Python版本的bisect_right（迭代版）:
def bisect_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


# 该库不支持key参数的操作，但DSU功能：装饰、排序(搜索)、去除装饰 模式(同用于list.sort)
seq = "I aim to misbehave".split()
dec = sorted((len(x), x) for x in seq)
keys = [k for (k, v) in dec]
vals = [v for (k, v) in dec]
print(vals[bisect_left(keys, 3)])


# 搜索树的遍历及其剪枝：二分法需要在常数时间内检测序列的中间值，这在链表中是做不到的
# 搜索树属性：对于某子树的根节点上的值都应该小于（或等于）r的值，而右子树上的值则要大于它
# 该树结构在set类型的实现中非常有用，若用映射表类型的话，得为每个节点都设置一个键、值对

# 二分搜索树中的插入与搜索
class Node:
    lft = None
    rgt = None

    def __init__(self, key, val):
        self.key = key
        self.val = val


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    return node


def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif key < node.key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)


class Tree:
    root = None

    def __setitem__(self, key, val): # 每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
        self.root = insert(self.root, key, val)

    def __getitem__(self, key): # 凡是在类中定义了这个__getitem__ 方法，那么它的实例对象（假定为p），可以像这样p[key] 取值，当实例对象做p[key] 运算时，会调用类中的方法__getitem__。
        return search(self.root, key)

    def __contains__(self, key): # 在Class里添加__contains__(self,x)函数,可判断我们输入的数据是否在Class里.参数x就是我们传入的数据.
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True
# 散列表（字典）比起有序数组、树更有优势，理论平均时间复杂度是常数级(其余是对数级)，但散列表会要求我们计算出相关对象的哈希值，有些情况不适合用散列表来做

# 选取算法：快速排序法的基础算法——在线性时间内找出一个无序序列中的第k大的数
# 在Python中，若要在一个可迭代容器中查找k个值最小(或值最大)的对象，且当k相对于对象总数量来说取值很小时，可用heapq模块中的nsmallest(或nlargest)函数，k取值较大是，可能需要先将序列排序
# 方法：在线性时间内将问题数据分成两半，而所有要找的对象在某一半中（简单的分割方式就是找出这些值中所谓的分割点来划分）

# 对这种划分与选取算法的一种简单实现
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi, k-m-1)
    else:
        return select(lo, k)

# 折半排序
# Python本身list.sort()效率足够好，还提供了业界最好的排序算法（Timsort）
# 快速排序法(快速选取法的扩展)：针对每个k提出一个解决方案，找出序列最小的元素，第二小的元素，一直找下去，并将这些元素放到各自合适的位置上

# 快速排序
def quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi) # 在平均情况下是个线性对数级算法，而在最坏情况下是个平方级算法

# 归并排序：先在一个有序序列中插入单个元素，最后把两个有序序列归并起来
def mergesort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

# 对于排序来说，归并排序这类分治算法已经属于最优状态了

"""三个额外的实例"""

# 最近点对问题：某平面中存在一些点，我们要在其中找出距离最接近的一对点(线性级)——类似归并

# 凸包问题：若我们在一块板上钉了n个钉子，然后用一个橡皮圈将其为了起来，计算能容纳这些点的最小凸形区域——关键是找出这些点上下边界的公共切线

# 最大切片问题：需要在一个实数序列中截取一个切片（或者片段）A[i:j],是A[i:j]的和值是该序列所有片段中最大的

"""树的平衡与再平衡"""
# 各种树结构及其再平衡方法都不尽相同，但通常都由两类基本操作发展而来：1.节点的分割与合并 2.节点的翻转
# 2-3树：允许一个节点拥有一到两个键，最多三个子节点，且该节点左子树的节点小于其最小键值，同时右子树的节点都要大于其最大键值，而中间子树上的节点值必须落在这两者之间
# 2-3树是B树的一种特殊情况，而B树几乎是所有数据库、基于磁盘的树形系统的基石
# AA树：较为简单的翻转平衡方案
# 用AA树结构实现再平衡的二分搜索树
class Node:
    lft = None
    rgt = None
    lvl = 1

    def __init__(self, key, val):
        self.key = key
        self.val = val

def skew(node):
    if None in [node, node.lft]:
        return node
    if node.lft.lvl != node.lvl:
        return node
    lft = node.lft
    node.lft = lft.rgt
    lft.rgt = node
    return lft

def split(node):
    if None in [node, node.rgt, node.ret.ret]:
        return node
    if node.rgt.rgt.lvl != node.lvl:
        return node
    rgt = node.rgt
    node.rgt = rgt.lft
    rgt.lft = node
    rgt.lvl += 1
    return rgt

def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    node = skew(node)
    node = split(node)
    return node

# 二分堆结构与heapq(C语言实现的模块)、heapsort
# 二分堆是一个完整的二叉树结构，意味它会始终保持平衡。堆属性：规定每个父节点的值都必须小于其所有的子节点(最小值堆，最大堆相反)
# heapq模块实现了一个非常有效率的堆结构，用list来实现，采用一种编码形式：若a是一个堆，那么a[i]的子节点就位于a[2*i+1]与a[2*i+2]两个位置，a[0]为根节点
#可用heappush()和heappop()两个函数从头构建一个堆结构，也可用heapify()从一个拥有大量元素项的列表开始，使之成为一个堆结构
from heapq import heappush, heappop
from random import randrange
Q = []
for i in range(10):
    heappush(Q, randrange(100))
print(Q)
print([heappop(Q) for i in range(10)])
# heapreplace函数：弹出堆中最下元素的同时插入一个新元素(更有效率)