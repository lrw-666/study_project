"""Python核心编程的相关学习"""
# 搜索：search()函数  匹配:match()函数
# 元字符：特殊符号与字符

# 择一匹配：|  匹配任意单个字符：. 起始匹配:^或\A 结尾匹配:$或\Z 转义:.*\$$ \b匹配单词边界模式 \B匹配包含出现在一个单词中间的模式
# 匹配特定某些字符:[] 限定范围和否定:-,^(脱字符)

"""闭包操作符"""
# 匹配一个、多个或没有出现的字符串模式：*(零次或多次,Kleene闭包) +(一次或多次，正闭包) ？(零次或一次)
# 匹配前面的正则表达式N次或一定方位的次数：{}
# 匹配尽可能少的次数：问号紧跟在任何使用闭合操作符的匹配后面
# 贪婪匹配：当模式匹配使用分组操作符时，正则表达式引擎将试图吸收匹配该模式尽可能多的字符

"""字符集特殊字符"""
# 十进制数字：\d  全部字符数字：\w 空格字符：\s 大写版本表示不匹配：\D

"""圆括号指定分组"""
# 功能：对正则表达书进行分组、匹配子组

"""扩展表示法"""
# 以问号开始：通常用于判断匹配前提供标记，实现一个前视或后视匹配，或条件检查

"""re模块"""
# 主要函数：match()函数、search()函数、compile()函数
# 使用compile()编译正则表达式
# 匹配对象：成功调用match()或search()返回的对象，有两个主要方法：group()和groups()

print("------------------------------------------1")
"""使用match()方法匹配字符串"""
# 从字符串起始部分对模式进行匹配，若匹配成功，就返回一个匹配对象，否则返回None
import re
m = re.match('foo', 'foo1')
if m:
    print(m.group())

print("------------------------------------------2")
"""使用search()在一个字符串中查找模式"""
# 在任意位置对给定正则表达式模式搜索第一次出现的匹配情况
m = re.search('foo', 'seafood')
if m:
    print(m.group())

print("------------------------------------------3")
"""匹配多个字符串"""
# 择一匹配(|)符号
bt = 'lrw|lqx|lrs'
m = re.match(bt, 'lrw')
if m:
    print(m.group())

m = re.search(bt, 'Afternoon, lrw is eating')
if m:
    print(m.group())

print("------------------------------------------4")
"""匹配任何单个字符"""
# 点号(.)，不能匹配一个换行符或者非字符，即空字符串,要找小数点就用反斜杠转义\
anyEnd = '.txt'
anyThing = '\.txt'
m = re.match(anyEnd, 'atxt')
if m:
    print(m.group())
m = re.search(anyEnd, 'book.txt')
if m:
    print(m.group())
m = re.search(anyEnd, 'bookatxt')
if m:
    print(m.group())

print("------------------------------------------5")
"""创建字符集[]"""
M = '[lmn][opq][rst]'
m = re.match(M, 'lqs')
if m:
    print(m.group())

print("------------------------------------------6")
"""重复、特殊字符以及分组"""
# 匹配邮件地址
M = '\w+@(\w+\.)?\w+\.com'
m = re.match(M, 'luorenwei1074@qq.com')
if m:
    print(m.group())
# 扩展：*
M = '\w+@(\w+\.)*\w+\.com'
m = re.match(M, 'luorenwei1074@hhh.bbb.aaa.qq.com')
if m:
    print(m.group())
# 匹配、保存子组
M = '\w\w\w-\d\d\d'
m = re.match(M, 'lrw-123')
if m:
    print(m.group())
M = '(\w\w\w)-(\d\d\d)'
m = re.match(M, 'lrw-123')
if m:
    print(m.group(1))
    print(m.groups())

print("------------------------------------------7")
"""匹配字符串的起始和结尾以及单词边界"""
# 以...开头
M = '^The'
m = re.search(M, 'The apple')
if m:
    print(m.group())
# 边界
M = r'\bthe' # \b在正则中表示单词间隔。但由于\b在字符串里本身是个转义，代表退格。r是得到字符本身。也就是说\b这两个字符。
m = re.search(M, 'hit the dog') # 有边界
if m:
    print(m.group())
M = r'\Bthe'
m = re.search(M, 'hitthe dog') # 无边界
if m:
    print(m.group())

print("------------------------------------------8")
"""使用findall()和finditer()查找每一次出现的位置"""
# findall()查询字符串中某个正则表达式模式全部的非重复出现情况，返回列表.finditer()类似,但更省内存，返回一个迭代器
print(re.findall('car', 'carry the barcardi to the car'))
s = 'This and that'
print(re.findall(r'(th\w+) and (th\w+)', s, re.I))
print([g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)])

print("------------------------------------------9")
"""使用sub()和subn()搜索与替换"""
# 将某字符串中所有匹配正则表达式的部分进行某种形式的替换，返回一个用来替换的字符串，subn()还返回一个表示替换的总数
print(re.sub('X', 'lrw', 'X\n is eating'))
print(re.subn('X', 'lrw', 'X is eating'))
print(re.sub('[ae]', 'X', 'abcdef'))
print(re.subn('[ae]', 'x', 'abcdef'))
# 除了用group方法取出匹配分组编号外，还可以使用\N,N是在替换字符串中使用的分组编号
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91'))
# 在限定模式上使用split()分隔字符串
print(re.split(':', 'str1:str2:str3'))
DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum)) # 若空格紧跟在五个数字(ZIP编码)或者两个大写字母后，就用split语句分割该空格

print("------------------------------------------10")
"""扩展符号"""
# (?iLmsux):直接在正则表达式里指定一个或者多个标记 如re.I/IGNORECASE不区分大小写 re.M/MULTILINE实现多行混合
print(re.findall(r'(?i)yes', 'yes? Yes. YES!!!'))
print(re.findall(r'(?im)(^th[\w ]+)', """This line is the first,
another line,
that line,
it's the best"""))
# re.S/DOTALLL 标记表明点号(.)能够用来表示\n符号
print(re.findall(r'(?s)th.+', """This line is the first
another line
that line
it's the best"""))
# re.X/VERBOSE 标记允许用户通过抑制在正则表达式中使用空白符(除了在字符类中或者在反斜线转义中)来创建更易读的正则表达式，此外散列、注释和井号可用于一个注释的起始
print(re.search(r'''(?x)
\((\d{3})\) # 区号
[ ] # 空白符
(\d{3}) # 前缀
- # 横线
(\d{4}) # 终点数字
''', '(800) 555-1212').groups())
# (?:...):可对部分正则表达式进行分组，但不会保存该分组用于后续的检索或者应用
# (?P<name>)和(?P=name):前者通过使用一个名称标识符而不是使用从1开始到N的增量数字来保存匹配，使用类似风格为\g<name>来检索
# (?=...)和(?!...)符号在目标字符串中实现一个前视匹配，前者为正向前视断言，后者为负向前视断言
# 条件正则表达式匹配：(?(id/name)Y|N)
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))

"""杂项"""
# 若有符号同时用于ASCII和正则表达式，就会发生问题，使用Python的原始字符串来避免产生问题
# 使用一个反斜线转义反斜线:\\b

"""一些正则表达式示例"""
"""匹配字符串"""
"""搜索与匹配还有贪婪"""
# 惰性匹配：使用“.+”来表明一个任意字符集跟在我们真正感兴趣的部分之后
# 正则表达式本质上实现贪婪匹配，试图获取匹配该模式的尽可能多的字符。
# 方案一：使用非贪婪操作符“？”，在“*”，“+”，“？”后使用该操作符
# 方案二：把“::”作为字段分隔符，使用strip('::')方法获取所有的部分，然后使用strip('-')作为另一个横线分隔符
# '.+'来表明一个任意字符集跟在我们感兴趣的部分之后
# 只想去除中间的那个整数：-(\d+)-