"""归纳、递归及归简"""
# 归简指将某一问题转化成另一个问题
# 归纳用于证明某个语句对于某种大型对象类是否成立(推广)
# 递归用于函数自我调用时

# 例：从数字列表中找出两个彼此最接近但不相等的数
from random import randrange
seq = [randrange(10**10) for i in range(100)]
dd = float("inf")
for x in seq:
    for y in seq:
        if x == y:
            continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d
# 优化：已排序的序列中最接近的两个数必然是相邻的
seq.sort()
dd = float(len(seq)-1)
seq.sort()
dd = float("inf")
for i in range(len(seq)-1):
    x, y = seq[i], seq[i+1]
    if x == y:
        continue
    d = abs(x-y)
    if d < dd:
        xx, yy, dd = x, y, d
# 将问题归简为找出某已排序序列中最接近的两个数(将问题分割为排序和扫描已排序的序列两部分)

# 归纳法其实就是先提出一个命题或语句P(n),再来证明它对任何自然数n都成立
# 弱归纳：将问题规模从n缩小到n-1
# 例：考察前n个数中的奇数之和，P(n)-> 1+3+5+...+(2n-3)(2n-1)=n**2(类似握手问题)
# 归纳法的思路是建立一条涵盖所有自然数的"扫描式"证据链，证明P(n-1)=>p(n)
# p(n-1)=1+3+5+...+(2n-3)=(n-1)**2 代入原式即可证明

# 递归法通常会从基本情况着手，并进一步证明相关的归纳步骤，将其推进到目标问题的整体规模n
# 例：棋盘问题
def cover(board, lab=1, top=0, left=0, side=None):
    if side is None:
        side = len(board)

    s = side // 2

    offsets = (0, -1), (side-1, 0)

    for dy_out, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top+dy_out][left+dx_outer]:
                board[top+dy_inner][left+s+dx_inner] = lab

    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(board, lab, top+dy, left+dx, s)
    return lab

board = [[0]*8 for i in range(8)]
board[7][7] = -1
print(cover(board))

# 将归纳和递归实现成某种迭代操作更好，因为迭代操作的开销通常比递归少一些，大部分编程语言的递归深度是有限的(栈的最大深度)
# 例：序列遍历(在range（1000)上运行，就会收到异常，超过了最大递归深度
def trav(seq, i=0):
    if i == len(seq):
        return
    trav(seq, i+1)
trav(range(100))
# 大多数函数式编程语言都实现有一种被称为尾递归优化的机制，会修改前面的函数，让他们不收栈深度的限制，一般是将递归调用重写成内部循环
# 任何递归函数都可以被重写成相应的迭代操作(反之亦然)

# 例：前n-1个元素已经完成排序，现要将第n个元素插入到正确的位置上
# 插入排序法(递归版)：
def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
# 插入排序法（迭代版）：
def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

# 例：先找到最大的元素，并其放在n的位置上，然后继续递归排序剩下的元素
# 选择排序法（递归版）
def sel_sort_rec(seq, i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)

# 选择排序
def sel_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]

"""基于归纳法(与递归法)的设计"""
# 寻找最大排列问题的递归算法思路的朴素实现（平方级实现）：
def naive_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A) # 浪费：B重复创建
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A
# 寻找最大排列问题(线性级):计数器的应用(哈希)
def max_perm(M):
    n = len(M)
    A = set(range(n))
    count = [0]*n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A

# 计数排序算法
from collections import defaultdict
def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C)+1):
        B.extend(C[k])
    return B
# 若其中有若干个值的键相等的话，它们之间保持原有的顺序，有这样属性的排序算法被称为稳定的
# 基数排序、分桶排序（线性级排序算法）

# 明星问题:在人群中找出一位明星人士(该明星比如说人群中的其他人，但人人都认识明星)
# 即研究某组依赖关系——例在某个多线程应用程序中，线程之间可能存在着某种环形依赖的等待关系(死锁)，
# 我们需要找出一个不需要等待任何线程但其他所有线程都要依赖的它的线程
# 核心表现形式为一个图结构，寻找的是一个其他节点对它都有入边，但自身没有出边的节点
# 朴素版的明星问题方案：
def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break
            if not G[v][u]:
                break
        else:
            return u
    return None
# 明星问题的解决方案(线性级)
def celeb(G):
    n = len(G)
    u, v = 0, 1
    for c in range(2, n+1):
        if G[u][v]:
            u = c
        else:
            v = c
    if u == n:
        c = v
    else:
        c = u
    for v in range(n):
        if c == v:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c
    return None

from random import randrange
# 图的构建操作是平方级的
n = 100
G = [[randrange(2) for j in range(n)] for i in range(n)]
c = randrange(n)
for i in range(n):
    G[i][c] = True
    G[c][i] = False
print(naive_celeb(G))
print(celeb(G))

# 拓扑排序问题：依赖关系易表示成一个有向非环路图(DAG)，寻找其中依赖顺序的过程称为拓扑排序
# 先移除其中一个节点，然后解决其余n-1个节点的问题
# 朴素的拓扑排序法
def naive_topsort(G, S=None):
    if S is None:
        S = set(G)
    if len(S) == 1:
        return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]:
            min_i = i+1
    seq.insert(min_i, v)
    return seq
# 有向无环图的拓扑排序（计数器）
def topsort(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0]
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
    return S

# Python的方法解析顺序MRO就是DAG的拓扑排序算法

# 松弛法与逐步完善
# 松弛法：通过逐步接近的方式来获得相关问题的最佳解法

# 归简法+换位法=困难度证明
# 困难度证明基于我们只允许用容易的归简法来简化问题：通过容易的归简法，我们可用解决B的方式来解决A
# 即：快速归简法+问题B的快速解决方案=问题A的快速解决方案
# 换位法：如果A是个难题，B就也是个难题

# 结论：
# 1.若我们能轻松地将问题A归简成B，那么B的困难度不会低于A
# 2.若我们想通过已知难题Y证明X是个难题，那就应该将Y归简成A