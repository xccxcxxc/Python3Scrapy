import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root',
                     password='', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO student(id, name, age) values (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
    print('Insert successfully')
except:
    print('Insert fail.')
    db.rollback()
db.close()
