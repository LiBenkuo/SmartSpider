# 爬虫进阶

## Day One
### Get 

```
import urllib2

url = "http://www.libenkuo.com"

response = urllib2.urlopen(url)

print response.read()
```

### Post

```
import urllib
import urllib2

url = "http://www.libenkuo.com"

form = {}
form_data = urllib.urlencode(form)

request = urllib2.Request(url, form_data)
response = urllib2.urlopen(request)

print response.read()
```
