# Beautiful Soup

## INSTALL

```
$ pip install beautifulsoup4
```

## 对象的种类

Beautiful Soup 将HTML文档转换成一个`树形结构`。
每个节点都是一个`Python 对象`，归纳为4种：

- Tag
- NavigableString
- BeautifulSoup
- Comment

### Tag

与 XML 或 HTML 原生文档中的 tag 相同

#### Name

#### Attributes

##### 多值属性

### NavigableString (可以遍历的字符串)

### BeautifulSoup

### Comment（注释及特殊字符串）

一个特殊类型的NavigableString对象。

## 遍历文档树

### 子节点

### 父节点

### 兄弟节点

### 回退和前进


## 搜索文档树

### 过滤器

### find_all()

### 像调用 find_all() 一样调用 tag

### find()

### find_parents() 和 find_parent()

### find_next_siblings() 和 find_next_sibling()

### find_previous_siblings() 和 find_previous_sibling()

### find_all_next() 和 find_next()

### find_all_previous() 和 find_previous()

### CSS 选择器

## 输出

### 格式化输出

### 压缩输出

### 输出格式

### get_text()

## 指定文档解析器

### 解析器之间的区别

## 编码

### 输出编码

### Unicode, Dammit


