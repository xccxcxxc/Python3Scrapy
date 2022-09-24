import pymysql

table = 'student'
condition = 'age > 20'

db = pymysql.connect(host='localhost', user='root',
                     password='', port=3306, db='spiders')
cursor = db.cursor()
sql = f'DELETE FROM {table} WHERE {condition}'
print(sql)
try:
    cursor.execute(sql)
    print('Successful')
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
