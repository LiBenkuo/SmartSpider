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
  # 逗号 之后不能带空格
  Order allow,deny
  Allow from all
</Directory>

# 添加 .py 后缀
AddHandler cgi-script .cgi .pl .py
```

## HTTP 头部

- Content-type:                 请求的与实体对应的MIME信息
- Expires: Date                 响应过期的日期和时间
- Location: URL                 用来重定向接收方到非请求URL的位置来完成请求或标识新的资源
- Last-modified: Date           请求资源的最后修改时间
- Content-length: N             请求的内容长度
- Set-Cookie: String            设置Http Cookie

## CGI 环境变量

- CONTENT_TYPE
> 指示所传递来的信息的MIME类型
> application/x-www-form-urlencoded 表示来自HTML表单

- CONTENT_LENGTH
> 如果服务器与CGI程序信息的传递方式是POST
> 这个环境变量即是从标准输入STDIN中可以读到的有效数据的字节数
> 在读取输入的数据时必须使用

- HTTP_COOKIE
> 客户机内的 COOKIE 内容

- HTTP_USER_AGENT
> 提供了包含了版本号或其他专有数据的客户浏览器信息

- PATH_INFO
> 表示紧接在CGI程序名之后的其他路径信息
> 常常作为CGI程序的参数出现

- QUERY_STRING
> GET 参数

- REMOTE_ADDR
> 发送请求的客户机的IP地址
> Web客户机需要提供给Web服务器的唯一标识
> 可以在CGI中用它来区分不同的Web客户机

- REMOTE_HOST
> 发送CGI请求的客户机的主机名

- REQUEST_METHOD
> 脚本被调用的方法

- SCRIPT_FILENAME
> CGI脚本的完整路径

- SCRIPT_NAME
> CGI脚本的名称

- SERVER_NAME
> WEB服务器的主机名、别名或IP地址

- SERVER_SOFTER
> 调用CGI程序的HTTP服务器的名称和版本号

```python
import os

for key in os.environ.keys():
	print key, os.environ(key)

```
