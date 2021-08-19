"""遍历：算法学中的万能钥匙"""
# 深度优先算法、广度优先算法、相关图中的强连通分量(一个图中的任何一个节点都有一条路径可以到达其他各个节点，那么它就是连通的)

# 遍历一个表示为邻接集的图结构的单个连通分量
from collections import deque


def walk(G, s, S=set()):
    P, Q = dict(), set() # set类型对象可让我们在其他类型上执行某些集合操作
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S): # difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
            Q.add(v)
            P[v] = u
    return P # 返回一个已被访问过的前趋节点的映射集(递归树)

# 找出无向图图的连通分量
def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        C = walk(G, u)
        seen.update(C) # update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
        comp.append(C)
    return comp

# 递归的树的遍历（无环，该树由标准的图结构来描述）
def tree_walk(T, r):
    for u in T[r]:
        tree_walk(T, u)

# 回归的运行轨迹称为回溯
# 停止循环遍历的方式(环路)：每次进入或离开一个十字路口时留下一个标准就可

# 递归版的深度优先搜索（DFS），利用LIFO先进后出
def rec_dfs(G, s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)

# 然后递归函数都是可以用迭代操作来重写的，一种方法是用我们自己的栈来模拟调用栈，可避免调用栈被塞满的问题

# 迭代版深度优先搜索（有向）：
def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u]) # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值
        yield u

# 通用性的图遍历函数
def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

# 可利用list很容易的定义栈（pop,add）
class stack(list):
    add = list.append

# 深度优先的时间戳与拓扑排序(再次）
# 在DFS树，任意节点u下所有后代节点都将会在u开始被探索到完成回溯操作之间的这段时间被处理
# 带时间戳的优先搜索
def dfs(G, s, d, f, S=None, t=0):
    if S is None:
        S = set()
        d[s] = t
        t += 1
        S.add(s)
    for u in G[s]:
        if u in S:
            continue
        t = dfs(G, u, d, f, S, t)
    f[s] = t
    t += 1
    return t

# DFS的属性：每个节点在DFS数中该节点的各个后代节点被探索之前被发现以及完成处理之后被完成
# 基于深度优先搜索的拓扑排序：
def dfs_topsort(G):
    S, res = set(), []
    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

# 无限迷宫与最短（不加权）路径问题——在一个既定状态空间内寻找解决方案
# 迭代深度的深度优先搜索算法IDDFS，是一种运行深度受到限制的、有限深度递增的DFS算法
# IDDFS（内部函数recurse基本上是一个深度受限制为d的递归版DFS算法）
def iddfs(G, s):
    yielded = set()
    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0:
            return
        if S is None:
            S = set()
        S.add(s)
        for u in G[s]:
            if u in S:
                continue
            for v in recurse(G, u, d-1, S):
                yield v
    n = len(G)
    for d in range(n):
        if len(yielded) == n:
            break
        for u in recurse(G, s, d):
            yield u

# 广度优先搜索算法BFS(遍历先进先出队列FIFO)
def bfs(G, s):
    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P
# 若想获取从a到u的路径，只要在队列P中往回倒就行
#
# path = [u]
# while P[u] is not None:
#     path.append(P[u])
#     u = P[u]
# path.reverse()

# list类型能胜任stack角色，但不能胜任queue角色，因为append操作时间为常量级，但从前端pop的操作时间则是线性级的
# 在BFS这类算法中，使用一种两端式队列，通常用链表或环状缓冲区来实现
# deque类实现一个块空间的双向链表，其中每个独立元素都是一个数组

# 强连通分量:SCCs 让有向路径上所有节点彼此到达的最大子图
# 一般情况下，只要任何一个强分量x中有一条边通往另一个强分量Y，x中最后完成遍历的时间一定会晚于Y中最后完成的时间——>无法采用从B到A的遍历方式
# 1.在目标图结构上执行dfs_topsort函数，并产生一个序列seq 2.翻转图中所有的边线 3.从seq中选择一个起点进行完全遍历
# DAG——有向无环图
# Kosaraju的查找强连通分量算法
def tr(G):
    GT = {}
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT
def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen:
            continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs

# 目标导向型搜索：查找某个特定节点，并尽可能忽略细节(修剪)