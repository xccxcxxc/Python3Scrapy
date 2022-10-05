import pymysql

data = {
    'id': '20120002',
    'name': 'Bob2',
    'age': 21
}
table = 'student'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root',
                     password='', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(
    table=table, keys=keys, values=values)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update
print(sql)
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        db.commit()
        print('Successful')
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
