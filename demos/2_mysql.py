
import pymysql
from pymysql.cursors import DictCursor
conn = pymysql.connect(
    user='root',
    password='admin123',
    host='localhost',
    database='crawl',
)
# 差
# cursor = conn.cursor(DictCursor)
# cursor.execute('select * from manger')
# r = cursor.fetchall()
# print(r)

# 增
cursor = conn.cursor()
name = '小芳'
money = 100
# sql = f"insert into manger(name,money) values('{name}',{money})"

# 可以避免sql被注入的危险
sql = f"insert into manger(name,money) values(%s,%s)"

cursor.execute(sql, (name, money))
conn.commit()
