import pymysql

data = {
    'id': '20120002',
    'name': 'Bob2',
    'age': 22
}
table = 'student'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root',
                     password='', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
    table=table, keys=keys, values=values)
# print(sql)
try:
    if cursor.execute(sql, tuple(data.values())):
        db.commit()
        print('Successful')
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
