__author__ = 'mocy'
#coding:UTF-8
import requests
from bs4 import BeautifulSoup
import pymysql
import re

#豆瓣电影爬取热映电影
def getHotMovie():
    res = requests.get('https://movie.douban.com/')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    rynow = soup.select('.ui-slide-content')#获取热映列表
    return rynow
#数据库基本配置
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'root',
          'db':'spider',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
db = pymysql.connect(**config)
#创建游标
cursor = db.cursor()

#表存在判断函数
def exits_of_table(table_name):
    cursor.execute('USE spider')
    sql_show_table = 'SHOW TABLES;'
    cursor.execute(sql_show_table)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return True
    else:
        print('no exits')
        return False

table_name = 'doubanmovie1'
if(exits_of_table(table_name)):
    print('database is exits')
else:
    #预处理语句
    ctsql = """CREATE TABLE doubanmovie1(
         movieid  INT  AUTO_INCREMENT,
         moviename  VARCHAR(50),
         movieimg VARCHAR(100) ,
         movierating FLOAT(6,2) ,
         PRIMARY KEY (movieid)
          )"""
    cursor.execute(ctsql)
rynow = getHotMovie()#调用函数获取热映电影
times = 0
for r in rynow:
    #有些电影暂无评分，所以我们根据海报数量创建列表
    for i,poster in enumerate(r.select('.poster img')):
        times = i
#创建列表存储爬取到的数据
list = [[0 for col in range(3)] for row in range(times+1)]
#修改列表的值
for r in rynow:
        for i,poster in enumerate(r.select('.poster img')):
             #提取属性
             list[i][0] = poster['src']#海报地址
        for i,title in enumerate(r.select('.title a')):
             list[i][1] = title.text#标题
        for i,rating in enumerate(r.select('.rating .subject-rate')):
             list[i][2] = rating.text#评分
#
#数据库操作批量插入数据
sql = "INSERT INTO doubanmovie1(movieimg, moviename, movierating) VALUES (%s,%s,%s)"
try:
    # 执行sql语句
    cursor.executemany(sql, list)
    # 提交到数据库执行
    db.commit()
except :
    # 如果发生错误则回滚
    db.rollback()
cursor.close()#游标关闭
db.close()#数据库关闭