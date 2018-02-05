__author__ = 'mocy'
#coding:UTF-8
import pymysql.cursors
from datetime import date,datetime,timedelta
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'root',
          'db':'shop',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
# Connect to the database
conn = pymysql.connect(**config)

#执行sql
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from cate")
result = cursor.fetchall()
# print(result)
for i in result:
    for j in i.keys():
        print(i.get(j))
    print('------------')
# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


