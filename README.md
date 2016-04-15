# 爬虫进阶
> 在 Python 的世界里，实现一个智能爬虫

## `Python2` OR `Python3`

`Scrapy` —— 一个Python开发的快速、高层次的Web抓取框架。

截止`2016-04-12`的`Scrapy1.0`要求`Python2.7`。

所以，果断选`Python2`。

## [Scrapy Install](http://doc.scrapy.org/en/1.0/intro/install.html)

> Latest versions of python have `pip` bundled with them so you won't need to install it separately.

```shell
$ pip install scrapy
```

Oooops，`Mac OS X` 下出错
```
Failed building wheel for lxm
```

解决方法：
```shell
$ xcode-select --install
```

重新安装，成功！


