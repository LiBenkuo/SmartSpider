# Python 操作 MySQL 数据库

## module `MySQLdb`

```
$ pip install MYSQL-python
```

## Python DB API

### connection —— 数据库连接对象

### cursor —— 数据库交互对象

用于执行查询和获取结果

- excute(op[, args])
> 执行一个数据库查询
> 执行 SQL 将结果从数据库获取到客户端

- fetchxxx()
> rownumber(相当于指针)

- fetchone()
> 取得结果集的下一行

- fetchmany(size)
> 获取结果集的下几行

- fetchall()
> 取得结果集中剩下的所有行

- rowcount
> 最近一次execute返回数据的行数或影响行数

- close()
> 关闭


### exceptions —— 数据库异常类
