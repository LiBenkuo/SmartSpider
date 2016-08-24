# CGI(Common Gateway Interface)

通用网关接口，它是一段程序，运行在服务器上，如：HTTP服务器，提供给客户端HTML页面的接口。



## Web服务器支持及配置

### Apache

### 设置CGI目录

```
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
```

所有的HTTP服务器执行的CGI程序，都保存在一个预先配置的目录。
这个目录被称为CGI目录，按惯例命名为`/var/www/cgi-bin`

CGI文件的扩展名为 `.cgi` ，Python 也可以使用 `.py` 扩展名。

通过修改 `httpd.conf` 指定其他运行 `cgi` 脚本的目录：
```
<Directory "/var/www/cgi-bin">
  AllowOverride None
  Options +ExecCGI
  Order allow, deny
  Allow from all
</Directory>

# 添加 .py 后缀
AddHandler cgi-script .cgi .pl .py
```


