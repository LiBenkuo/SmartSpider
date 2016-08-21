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


rs = cursor.fetchall()

for row in rs:
	print "userid=%d, username=%s pwd=%s" % row

# Internet resource should be released
cursor.close()
conn.close()
