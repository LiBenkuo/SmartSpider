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

print conn
print cursor

# Internet resource should be released
cursor.close()
conn.close()
