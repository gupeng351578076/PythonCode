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
#创建游标
cursor = db.cursor()

#sql执行
sql = 'DROP TABLE IF EXISTS EMPLOYEE'
cursor.execute(sql)
#预处理语句
ctsql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(ctsql)
cursor.close()
db.close()