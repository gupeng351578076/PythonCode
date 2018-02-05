__author__ = 'mocy'
#coding:UTF-8
import pymysql
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'root',
          'db':'shop',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
db = pymysql.connect(**config)

cursor = db.cursor()
sql = 'SELECT VERSION()'
cursor.execute(sql)
data = cursor.fetchone()
print(data)
cursor.close()
db.close()