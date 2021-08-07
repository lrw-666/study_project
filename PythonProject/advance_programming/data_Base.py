"""数据库编程"""
# 持久化存储(3种机制)：文件、数据库系统以及一些混合类型
# 访问数据库包括直接通过数据库接口访问和使用ORM访问两种方式。Python中数据库是通过设配器的方式进行访问的，适配器是一个Python模块
# Python的数据库API(DB-API)：阐明一系列所需对象和数据库访问机制的标准，可为不同的数据库适配器和底层数据库系统提供一致性的访问
# connect()函数属性：用户名user、密码password、主机名host、数据库名database、数据源名dsn
# Connection对象：建立连接，方法->close(),commit(),rollback(),cursor(),errorhandler()
# Cursor对象（游标）:和数据库通信，游标对象，最重要的属性为execute()和fetch()方法，支持存储过程：callproc()

# 连接MySQL：设配器——MySQLdb（python2） pymysql或者mysqlclient(python3)
import pymysql
# cxn = pymysql.connect(user='root', passwd='root')
# cxn.query('CREATE DATABASE test1')
# cxn.commit()
# cxn.close()
# 此处未使用游标，commit方法是可选的，MySQL默认开启了自动提交

# pymysql.Connect()参数说明
# host(str):      MySQL服务器地址
# port(int):      MySQL服务器端口号
# user(str):      用户名
# passwd(str):    密码
# db(str):        数据库名称
# charset(str):   连接编码
#
# connection对象支持的方法
# cursor()        使用该连接创建并返回游标
# commit()        提交当前事务
# rollback()      回滚当前事务
# close()         关闭连接
#
# cursor对象支持的方法
# execute(op)     执行一个数据库的查询命令
# fetchone()      取得结果集的下一行
# fetchmany(size) 获取结果集的下几行
# fetchall()      获取结果集中的所有行
# rowcount()      返回数据条数或影响行数
# close()         关闭游标对象

"""标准格式："""
# 连接数据库
connect = pymysql.Connect(host='localhost', port=3306, user='root',
                          passwd='root', db='test1', charset='utf8')
# 获取游标
cursor = connect.cursor()
# 建立表
sql = "create table Py(pid INT, name CHAR(20), price INT);"
cursor.execute(sql)
connect.commit()

# 插入数据
sql = "INSERT INTO Py (pid, name, price) VALUES (%d, '%s', %d)"
data = (1, 'lrw', 555)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')

# 修改数据
sql = "UPDATE Py SET price = %d WHERE name = '%s'"
data = (999, 'lrw')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')

# 查询数据
sql = "SELECT pid,name, price FROM Py WHERE pid=%d"
data = 1
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("pid:%d\tname:%s\tpid:%d" % row)
print('共查出', cursor.rowcount, '条数据')

# 删除数据
sql = "DELETE FROM Py WHERE pid = %d"
data = 1
cursor.execute(sql % data)
connect.commit()
print('成功删除', cursor.rowcount, '条数据')


# 事务处理
sql1 = "UPDATE Py SET name = 'hhh' WHERE pid=1"
sql2 = "UPDATE Py SET name = 'ggg' WHERE pid=2"
sql3 = "UPDATE Py SET name = 'fff' WHERE pid=3"
try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
except Exception as e:
    connect.rollback() # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit() # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()

""" ORM 系统"""
# 对象关系映射（英语：Object Relational Mapping，简称ORM，或O/RM，或O/R mapping），是一种程序设计技术，用于实现面向对象编程语言里不同类型系统的数据之间的转换。
# 从效果上说，它其实是创建了一个可在编程语言里使用的“虚拟对象数据库”。如今已有很多免费和付费的ORM产品，而有些程序员更倾向于创建自己的ORM工具
# 面向对象：更愿意操纵Python对象而不是SQL查询的程序员 让用户更多地通过'对象’的方式来避免SQL语句
# ORM系统的作者将纯SQL语句进行了抽象化处理，即将数据库表转化为Python类，其中的数据列作为属性，而数据库操作作为方法
# Python ORM：SQLAlchemy和SQLObject等等

"""非关系数据库"""
# 非关系数据库：对象数据库、键-值数据库、文档存储、图形数据库、表格数据库、列/可扩展记录/宽列数据库、多值数据库
# 可扩展性问题最终造就了非关系数据库或者NoSQL数据库的创建、爆炸性增长以及部署
# 如今有一个非常流行的文档存储非关系数据库叫做MongoDB
# 文档存储讨论文档、集合等等，将数据存储于特殊的JSON串(文档)中，类似于一个Python字典，是一个二进制编码的序列化
# PyMongo