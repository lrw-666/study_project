"""文本处理"""
# Python标准库含有3个文本处理模块和包：csv、json、xml
# 逗号分隔值(CSV)
import csv
# 例：获取数据，以CSV格式输出到文件中，接着将同样的数据读回
DATA = (
    (9, 'Web Clients and Servers', 'base64, urllib'),
    (10, 'Web Programming: CGI & WSGI', 'cgi, time, wsgiref'),
    (13, 'Web Services', 'urllib, twython'),
)
# 脚本接收三元组，将对应的记录作为CSV文件写到磁盘上，接着读取并解析刚写入的CSV数据
print('*** WRITING CSV DATA')
f = open('bookdata.csv', 'w') #  open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写
writer = csv.writer(f)
for record in DATA:
    writer.writerow(record) # 在打开的文件中逐行写入逗号分隔的数据
f.close()
print('*** REVIEW OF SAVED DATA')
f = open('bookdata.csv', 'r')
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()
# csv模块还提供了csv.DictReader类和csv.DictWriter类，用于将CSV数据读进字典中

# JSON:是JavaScript的子集，专门用于轻量级的数据交换方式，是以人类更易读的方式传输结构化数据,很像Python的字典
# 注：JSON值理解Unicode字符串
import json
from pprint import pprint
# 功能基本一样 pprint()模块打印出来的数据结构更加完整，每行为一个数据结构，更加方便阅读打印输出结果。特别是对于特别长的数据打印，print()输出结果都在一行，不方便查看，
# 而pprint()采用分行打印输出，所以对于数据结构比较复杂、数据长度较长的数据，适合采用pprint()打印方式。当然，一般情况多数采用print()
# Python字典转化成了JSON对象
print(dict(zip('abcde', range(5))))
print(json.dumps(dict(zip('abcde', range(5)))))
print(json.loads(json.dumps(dict(zip('abcde', range(5))))))
# 类似：Python列表或元组也可转成对应的JSON数组
print(list('abcde'))
print(json.dumps(list('abcde'))) # json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
pprint(json.loads(json.dumps(list('abcde')))) # json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）
print(json.loads(json.dumps((1, 2, 3, 4, 5))))
# json不使用单引号

# XML(可扩展标记语言)：仅是纯文本格式
# XML -RPC的客户端-服务器服务

"""Jython"""
# 其适合Python开发者在Java开发环境中使用Python快速开发方案原型，并无缝地集成到已有的Java平台。也可通过为Java提供一个脚本语言环境简化工作

"""Google+平台"""
# 开发者可利用API访问并搜索Google+的用户和动态