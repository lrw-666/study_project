"""计数初步"""
# Python求和式：
# x*sum(S) == sum(x*y for y in S)

# 两种赛制：循环赛、淘汰赛
# 循环赛：握手问题

# 龟兔赛跑：两个彼此的函数，一个增长的较慢，另一个快，计算差距
from random import randrange
n = 10**90
p = randrange(n)
print(p < n/2)

# 子集与排列组合
# 伪多项式(时间)算法:算法的运行时间可以解释为某个输入数值的某个多项式函数（如背包问题）
def is_prime(n):
    """检查质数（非多项式）"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 递归和递归式：某个函数直接或间接调用自己的操作
# 为从数学角度来描述递归算法的运行时间，就要通道递推等式，即递归关系 T(n)=T(n-1)+1
# 重复代入法(迭代法):若T(n)=T(n-1)+1=T(n-2)+1+1=T(n-2)+2 ——> T(n)=T(n-1)+1=T(n-2)+2=T(n-3)+3 ——> T(n)=T(n-i)+i

"""一些重要的递归式"""
# 序列化处理问题，如归简操作：T(n)=T(n-1)+1
# 握手问题：T(n)=T(n-1)+n
# 汉诺塔问题：T(n)=2T(n-1)+1
# T(n)=2T(n-1)+n
# 二分搜索问题:T(n)=T(n/2)+1
# 随机选择问题、平均情况问题:T(n)=T(n/2)+n
# 树的遍历问题：T(n)=2T(n/2)+1
# 利用分治法处理问题： T(n)=2T(n/2)+n

# 解决问题的步骤:
# 1.逐步展开递归式，一直到我们发现其中的模式为止
# 2.将该模式表示出来(通常会涉及一个求和式)，并用变量i表示行号
# 3.根据i层递归将会达到基本情况来选择i的值(并解决该求和式)

# 如递归式5：
# 1.T(n)=T(n/2)+1=T(n/4)+1+1=T(n/8)+1+1+1
# 2.T(n)=T(n/2**i)+i
# 使T(n/2**i)——>T(1)

# 递归式7和8为多重递归调用

#猜测与检验：证明一个递归式解决方案的正确性
# 强归纳和弱归纳

# 跳进兔子洞(更改我们的变量)——替换T和n
# 递归式：T(n)=aT(n**1/b)+f(n) 设f(n)=lgn, b=2 则T(n)=2T(n**1/2)+lgn
# 令m=lgn,T(2m)=2T((2**m)**1/2)+m=2T(2**m/2)+m
# 令S(m)=2S(m/2)+m

# 主定理：一刀切式的解决方案
# 递归式与分治法对应关系的一般形式：T(n)=aT(n/b)+f(n)
# 三种情况：大部分查找都运行在根节点上、叶节点上或均匀分布在该递归树的各行之间

# 排序算法之侏儒排序法
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

# 排序算法之归并排序法
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

seq = [0, 5, 1, 3, 2]
print(mergesort(seq))