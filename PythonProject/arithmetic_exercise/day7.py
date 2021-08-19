"""复杂依赖及其记忆体化--动态规划DP"""
# 动态：事情会随着时间演变
# 规划：完成一组选择("线性规划")
# 核心：一种高速缓存，通常情况下，通过反转相应的递归函数，使其对某些数据结构进行逐步迭代和填充
# 另一种选择：记忆体化——在实现相关递归函数时直接从缓存中返回值。若可用同一个参数执行多次调用，其返回结果就会直接来自缓存
# 例：找出一组数字的最长递增子序列
# 朴素版的最长递增子序列算法：
from itertools import combinations
def naive_lis(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return sub
# 编程工作中最基本、最重要的原则之一：不要重复自己
# 斐波那契数列的递归定义：从两个1开始，每次增加的元素为前两个元素之和
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)

# 记忆体化的装饰器函数(可当做一种装饰器来设计 )
# Python装饰器（decorator）在实现的时候，有一些细节需要被注意。例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变)
# functools模块的lru_cache函数，将其maxsize参数设置为None，就是一个完全运用记忆体的装饰器函数，等价
from functools import wraps
def memo(func):
    cache = {}
    @ wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

fib = memo(fib)
print(fib(100))# 单独写会报错

# 内存化函数的思路就是缓存器自身的返回值
@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)
print(fib(100))

# 例求2的指数
@memo
def two_pow(i):
    if i == 0:
        return 1
    return two_pow(i-1) + two_pow(i-1)
print(two_pow(100))
# 或修改：
def two_pow(i):
    if i == 0:
        return 1
    return 2*two_pow(i-1)
print(two_pow(100)) # 降低递归调用的数量

# 二项式系数的计算：组合函数C(n, k)表示从含n个数的集合中找出k个数大小的子集数
# 动态规划解决问题：判断元素是否被包含在内来分解问题(递归调用只有在相关元素被包含其中才会被调用)
# （n,k)=(n-1,k-1)+(n-1,k) C（n,0）=1  C(0,k)=0

# 帕斯卡三角形路径计数
@memo
def C(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    return C(n-1, k-1) + C(n-1, k)
print(C(4, 2))

# 对于大多数问题而言，记忆体处理所代表的就是指数级运算与多项式级运算之间的差别
# 大多数动态规划陈述中，记忆体函数实际上不是拿来用的，其中的递归分解的确是算法设计的一个重要步骤，
# 但它通常只是一个数学工具，主要用来实现版本的反转——迭代版，不仅能运行的更快，还可避免因递归深度过大而导致堆栈空间耗尽
# 而且迭代版本通常会实现一个专属构造的缓存，而不是@memo中看到的那种通用的"由参数元组组成的键值字典"

# 反转帕斯卡三角形，用defaultdict来缓存
# defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，
# 即工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0
from _collections import defaultdict
n, k = 10, 7
C = defaultdict(int)
for row in range(n+1):
    C[row, 0] = 1
    for col in range(1, k+1):
        C[row, col] = C[row-1, col-1] + C[row-1, col]
print(C[n, k])

# 有向无环图中的最短路径问题
# 贪心算法之基于当下做出最好的选择，并没有考虑全局
# 动态规划核心是一个决策顺序的问题，我们每个选择都会导致一个新的局面，所以我们需要根据自己所期望的局面来找出最好的选择顺序

# 寻找一个有向无环图中某一点到另一点的路径就是一个经典的决策顺序问题
# 我们将决策每一个可能的决策状态都视为一个独立的节点，其中的出边则代表我们在各种状态下所可能做出的选择，
# 这些边都赋予了权值，要找出最佳决策集就是该图的最短路径

# 运用递归、记忆体化的方法来解决DAG的最短路问题
def rec_dag_sp(W, s, t): # 从s到t
    @memo
    def d(u):
        if u == t:
            return 0
        return min(W[u][v] + d(v) for v in W[u])
    return d(s)

# 迭代版的DAG最短路径算法采用了松弛法，即通过逐步扩展局部方案来解决问题
# 关注自己从哪里来，确保自己一定能到达节点v。隐式地执行了一次DFS遍历，并按其遍历顺序来自动化地执行所有的更新
# DAG的最短路径问题
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

def dag_sp(W, s, t):
    d = {u: float('inf') for u in W}
    d[s] = 0
    for u in topsort(W):
        if u == t:
            break
        for v in W[u]:
            d[v] = min(d[v], d[u]+W[u][v])
    return d[t]
# 该迭代算法的思路是尽量松弛化出自我们之前所有可能节点的边，为此，我们必须对当前节点的入边进行松弛化

# 最长递增子序列：只需要看当前元素之前的元素是否都小于当前元素即可
# 用记忆体、递归方式解决最长递增子序列问题
def rec_lis(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1+L(pre))
        return res
    return max(L(i) for i in range(len(seq)))

# 用基本迭代方式解决最长递增子序列问题
def basic_lis(seq):
    L = [1]*len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1+L[pre])
    return max(L)
# DAG思路：将序列中每个元素都视为图中一个节点，并且每个节点到比他大的节点之间都会存在一条隐藏的边——对于所有符合条件的候选节点，都会存在一个递增子序列
# 即DAG的最长路径问题
# 重要思路：若我们有一个长度为m的子序列，其终点有不止一个前辈节点，保留最小的安全
from bisect import bisect # 用于排序、二分查找
def lis(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    return len(end)

# 序列对比问题：如两个序列之间的最长公用子序列（LCS）与其编辑距离两个问题
# 用递归、记忆体方式解决LCS问题
def rec_lcs(a, b):
    @memo
    def L(i, j):
        if min(i, j) < 0:
            return 0
        if a[i] == b[j]:
            return 1+L(i-1, j-1)
        return max(L(i-1, j), L(i, j-1))
    return L(len(a)-1, len(b)-1)

# 用迭代方式解决LCS问题
def lcs(a, b):
    n, m = len(a), len(b)
    pre, cur = [0]*(n+1), [0]*(n+1)
    for j in range(1, m+1):
        pre, cur = cur, pre
        for i in range(1, n+1):
            if a[i-1] == b[j-1]:
                cur[i] = pre[i-1]+1
            else:
                cur[i] = max(pre[i], cur[i-1])
    return cur[n]

# 解决问题的模式：以某种形式来定义问题的子问题，递归这些子问题之间的关系，然后确保每个子问题都只被计算一次(通过隐式或显式的记忆体化处理)
# 用递归、记忆体化方式解决无限制的整数背包问题
def rec_unbounded_knapsack(w, v, c): # 质量、价值、容量
    @memo
    def m(r):
        if r == 0:
            return 0
        val = m(r-1)
        for i, wi in enumerate(w):
            if wi > r:
                continue
            val = max(val, v[i] + m(r-wi))
        return val
    return m(c)

# 用迭代方式解决无限制的整数背包问题(用list来充当缓存)
def unbounded_knapsack(w, v, c):
    m = [0]
    for r in range(1, c+1):
        val = m[r-1]
        for i, wi in enumerate(w):
            if wi > r:
                continue
            val = max(val, v[i]+m[r-wi])
        m.append(val)
    return m[c]

# 0-1背包问题：每个对象最多只能用一次
# 用递归、记忆体化方式解决0-1背包问题
def rec_knapsack(w, v, c):
    @memo
    def m(k, r):
        if k == 0 or r == 0:
            return 0
        i = k-1
        drop = m(k-1, r)
        if w[i] > r:
            return drop
        return max(drop, v[i]+m(k-1, r-w[i]))
    return m(len(w), c)

# 用迭代方式解决0-1背包问题
def knapsack(w, v, c):
    n = len(w)
    m = [[0]*(c+1) for i in range(n+1)]
    P = [[False]*(c+1) for i in range(n+1)]
    for k in range(1, n+1):
        i = k-1
        for r in range(1, c+1):
            m[k][r] = drop = m[k-1][r]
            if w[i] > r:
                continue
            keep = v[i] + m[k-1][r-w[i]]
            m[k][r] = max(drop, keep)
            P[k][r] = keep > drop
    return m, P

# 序列的二元分割：
# 应用：矩阵连乘、解析与上下文无关的语言、最优搜索树
# 本质：按层次将序列分成区块，是其中的每一区块都包含另外两个区块，并同时找到能实现产生最佳性能或最佳值的划分方式
# 事情：选择中间值(或其中一个)作为分割点（根节点），然后递归创建左平衡子树和右平衡子树
# 用于实现最优搜索树的记忆体化递归函数
def rec_opt_tree(p):
    @memo
    def s(i, j):
        if i == j:
            return 0
        return s(i, j-1) + p(j-1)
    @memo
    def e(i, j):
        if i == j:
            return 0
        sub = min(e(i, r) + e(r+1, j) for r in range(i, j))
        return sub + s(i, j)
    return e(0, len(p))

# 用迭代方式解决最优搜索树问题
from collections import defaultdict
def opt_tree(p):
    n = len(p)
    s, e = defaultdict(int), defaultdict(int)
    for k in range(1, n+1):
        for i in range(n-k+1):
            j = i+k
            s[i, j] = s[i, j-1] + p[j-1]
            e[i, j] = min(e[i, r] + e[r+1, j] for r in range(i, j))
            e[i, j] += s[i, j]
    return e[0, n]