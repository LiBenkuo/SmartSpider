import urllib2

url = "http://www.libenkuo.com"

response = urllib2.urlopen(url)

print response.read()
