"""Dijkstra"""
# 对图的边采用松弛技术，将有关最短路径的知识扩展开
# 原理：把图表示为字典的字典，用字典D存放距离值估计（上界值），此外，增加一个前导节点字典P，构成最短路径树，帮助重建与D中距离对应的实际路径
# 松弛技术
from arithmetic_exercise.day7 import memo

inf = float("inf")
def relax(W, u, v, D, P):
    d = D.get(u, inf) + W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True
# 思想：通过途径u，查看是否可以缩短路径，从而改进目前已知的到达v点的最短路径

# Bellman-Ford算法（对所有的边反复进行松弛操作，直到确定一切答案正确为止）：用于任意有向或无向图的单源最短路径算法
def bellman_ford(G, s):
    D, P = {s: 0}, {}
    for rnd in G:
        changed = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    changed = True
        if not changed:
            break
    else:
        raise ValueError('negative cycle')
    return D, P
a, b, c, d, e, f, g, h = range(8)
G = {
    a: {b: 2, c: 1, d: 3, e: 9, f: 4},
    b: {c: 4, e: 3},
    c: {d: 8},
    d: {e: 7},
    e: {f: 5},
    f: {c: 2, g: 2, h: 2},
    g: {f: 1, h: 6},
    h: {f: 9, g: 8}
}

print(bellman_ford(G, a))

# 找到隐藏的DAG图，用到的拓扑排序是依据实际距离大小的节点排序(归纳法)
# 问题：路径有环
# 当一个节点可以成为最短路径的下个节点：这个节点拥有最短的距离值估计
# Prim算法中，优先级是向后来回遍历树的边的权值；在Dijkstra算法中，优先级是距离值估计

# Dijkstra算法：
from heapq import heappush, heappop
def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set() # est, tree, queue, visited
    while Q:
        _, u = heappop(Q)
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P

# 多对多问题——Johnson算法：将Bellman-Ford算法和Dijkstra算法结合，用于求解稀疏图
# 解决稀疏图所有节点对之间的最短路径问题，对从各个节点出发的情况使用Dijkstra算法
# 想法：增加一个新的节点s，它到所有现有节点的边权值为零，然后对从s出发的情况运行Bellman-Ford算法，这样可以计算出从s到图中每个节点的距离h(V)
# Johnson算法
from copy import deepcopy
def johnson(G):
    G = deepcopy(G)
    s = object()
    G[s] = {v: 0 for v in G}
    h, _ = bellman_ford(G, s)
    del G[s]
    for u in G:
        for v in G[u]:
            G[u][v] += h[u] - h[v]
    D, P = {}, {}
    for u in G:
        D[u], P[u] = dijkstra(G, u)
        for v in G:
            D[u][v] += h[v]-h[u]
    return D, P

# 牵强的子问题：分解解空间思想——把问题分解为子问题，再将子问题互相连接，构成子问题图
# 保证我们对子问题进行规模排序（拓扑排序）——无环
# Floyd-Warshall算法的缓存式递归实现
def rec_floyd_warshall(G):
    @memo
    def d(u, v, k):
        if k==0:
            return G[u][v]
        return min(d(u, v, k-1), d(u, k, k-1) + d(k, v, k-1))
    return {(u, v): d(u, v, len(G)) for u in G for v in G}

# Floyd-Warshall算法，仅考虑距离
def floyd_warshall(G):
    D = deepcopy(G)
    for k in G:
        for u in G:
            for v in G:
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
    return D

# Floyd-Warshall算法
def floyd_warshall2(G):
    D, P = deepcopy(G), {}
    for u in G:
        for v in G:
            if u == v or G[u][v] == inf:
                P[u, v] = None
            else:
                P[u, v] = u
    for k in G:
        for u in G:
            for v in G:
                shortcut = D[u][k] + D[k][v]
                if shortcut < D[u][v]:
                    D[u][v] = shortcut
                    P[u, v] = P[k, v]
    return D, P

# 中途相遇：若一开始就从起点和终点同时出发，展开遍历，这样的两组涟漪会在某些情况下中途相遇，从而节省大量工作(Dijkstra算法双向图版本)
# Dijkstra算法作为解决方案生成器的实现：
def idijkstra(G, s):
    Q, S = [(0, s), set()]
    while Q:
        d, u = heappop(0)
        if u in S:
            continue
        S.add(u)
        yield u, d
        for v in G[u]:
            heappush(Q, (d+G[u][v], v))

# 同时从两个节点s和t出发进行遍历操作，不断移动到下个距离最近的节点，所以一旦两个算法移动到（产生）相同的节点，结束遍历，但需要维护至今发现的最佳距离
# 最简单版本：一旦发现两组遍历返回相同节点，即终止算法运行，然后查找最佳路径，检查将两组遍历连在一起的所有边
# Dijkstra算法的双向图版本
from itertools import cycle
def bidir_dijkstra(G, s, t):
    Ds, Dt = {}, {}
    forw, back = idijkstra(G, s), idijkstra(G, t)
    dirs = (Ds, Dt, forw), (Dt, Ds, back)
    try:
        for D, other, step in cycle(dirs):
            v, d = next(step)
            D[v] = d
            if v in other:
                break
    except StopIteration:
        return inf
    m = inf
    for u in Ds:
        for v in G[u]:
            if not v in Dt:
                continue
            m = min(m, Ds[u]+G[u][v]+Dt[v])
    return m

# A*算法通过调整优先级，扩展Dijkstra算法
# Johnson算法对所有边权值加以变换，确保边权为正，且最短路径依然最短4
# A*以类似的方式对边进行修改，让远离目标节点的边权值大于那些离目标节点较劲的边
# A*算法相当于针对修正图的Dijkstra算法,可用于搜索解空间(抽象图、隐式图)
# A*算法
inf = float('inf')
def a_star(G, s, t, h):
    P, Q = {}, [(h(s), None, S)]
    while Q:
        d, p, u = heappop(Q)
        if u in P:
            continue
        P[u] = p
        if u == t:
            return d - h(t), P
        for v in G[u]:
            w = G[u][v] - h(u) + h(v)
            heappush(Q, (d+w, u, v))
    return inf, None

# 单词梯路径的隐式图
from string import ascii_lowercase as chars
def variants(wd, words):
    wasl = list(wd)
    for i, c in enumerate(wasl):
        for oc in chars:
            if c == oc:
                continue
            wasl[i] = oc
            ow = ''.join(wasl)
            if ow in words:
                yield ow
        wasl[i] = c

class WordSpace:
    def __init__(self, words):
        self.words = words
        self.M = dict()

    def __getitem__(self, wd):
        if wd not in self.M:
            self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
        return self.M[wd]

    def heuristic(self, u, v):
        return sum(a!=b for a, b in zip(u, v))

    def ladder(self, s, t, h=None):
        if h is None:
            def h(v):
                return self.heuristic(v, t)
        _, P = a_star(self, s, t, h)
        if P is None:
            return [s, None, t]
        u, p = t, []
        while u is not None:
            p.append(u)
            u = P[u]
        p.reverse()
        return p