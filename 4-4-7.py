import pymysql

sql = 'SELECT * FROM student WHERE age >= 20'

db = pymysql.connect(host='localhost', user='root',
                     password='', port=3306, db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One', one)
    results = cursor.fetchall()
    print('Results', results)
    print('Results Type', type(results))
    for row in results:
        print(row)
except Exception as e:
    print('Failed', e)

# 推荐使用以下方法逐条获取数据
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row', row)
        row = cursor.fetchone()
except:
    print('Error.')

db.close()
