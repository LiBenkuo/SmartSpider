import MySQLdb

conn = MySQLdb.Connect(
                       host = '127.0.0.1',
                       port = 3306,
                       user = 'superadmin',
                       passwd = 'test',
                       db = 'superadmin',
                       charset = 'utf8'
                      )

cursor = conn.cursor()

sql = "select * from USERS"
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs


rs = cursor.fetchall()
print rs

# Internet resource should be released
cursor.close()
conn.close()
