__author__ = 'mocy'
#coding:UTF-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='root', passwd='root', db='shop', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)"
# 一个tuple或者list
T = (('xiaoming', 31, 'b'), ('hong', 22, 'g'), ('wang', 90, 'm'))

try:
    # 执行sql语句
    cursor.executemany(sql, T)
    # 提交到数据库执行
    db.commit()
except :
    # 如果发生错误则回滚
    db.rollback()
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()