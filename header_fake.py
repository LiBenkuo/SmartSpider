import urllib2

headers = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'
}

request = urllib2.Request(
	url = 'http://www.libenkuo.com',
	headers = headers
)

print urllib2.urlopen(request).read()
