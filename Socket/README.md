# 网络编程

Python 提供的网络服务：
- 低级别
> 支持基本的 Socket
> 提供了标准的BSD Socket API
> 可以访问底层操作系统Socket接口的全部方法
- 高级别
> 模块 SocketServer
> 提供了服务器中心类
> 可以简化网络服务器的开发

## Socket

```
sokcet.socket([family[, type[, proto]]])
```

- family      AF_UNIX/AF_INET
- type        SOCK_STREAM/SOCK_DGRAM
- protocol    default 0


