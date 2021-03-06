# -*- coding: utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

from tempfile import TemporaryFile
from xlwt import Workbook

try:

	url = "http://www.gyfc.net.cn/pro_query/index/floorView.aspx?dongID=38395&danyuan=&qu=%B9%F3%D1%F4&yszh=2015120"
	url = "http://www.gyfc.net.cn/pro_query/index/floorView.aspx?dongID=13003394&danyuan=%25C8%25AB%25B2%25BF&qu=%25B0%25D7%25D4%25C6&yszh=2013055"

	# 伪造浏览器请求头
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
	}

	request = urllib2.Request(
		url = url,
		headers = headers
	)
	response = urllib2.urlopen(request)

	html = unicode(response.read(), 'gb2312').encode('utf-8')

	soup = BeautifulSoup(html, 'html.parser')

	# 格式化输出
	#print soup.prettify()

	book = Workbook(encoding='utf-8')
	sheet = book.add_sheet('销售信息')

	rowIndex = 0
	for saleInfo in soup.find_all('div', class_=re.compile('P0 W[1-9]|10 H0')):
		# print saleInfo

		if(saleInfo.find('span') == None):
			continue

		roomCode = saleInfo.find('span').string

		columnIndex = 0
		sheet.write(rowIndex, columnIndex, roomCode)
		#columnIndex += 1
		#sheet.write(rowIndex, columnIndex, roomCode[2:])
		
		for i in saleInfo['title'].split():
			columnIndex += 1
			sheet.write(rowIndex, columnIndex, i)
			
		rowIndex += 1	

	# 文件保存
	book.save('泰祥国际无单元.xls')
	book.save(TemporaryFile())
			
except urllib2.HTTPError, e:
	print e.code
	print e.msg
	print e.headers
	print e.fp.read()
