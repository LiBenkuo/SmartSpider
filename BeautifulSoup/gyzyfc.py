# -*- coding: utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

from tempfile import TemporaryFile
from xlwt import Workbook

try:

	url = "http://www.gzzyfc.com.cn/Client/ZunYi/Second/Detail/ProjectInfo/FloorHouse.aspx?id=nw6wrIdxdG%2bLhp2Ca%2b6tUnlnRqkh0eqtCLXj%2f9KYzJ6NvQnefxIeyZ0EjKlupA8RaBKdDAy4CSvH64JmXbcz4A%3d%3d"

	# 伪造浏览器请求头
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
	}

	cookie = "ASP.NET_SessionId=tsqpsaaae5sidexmckttbvwo"

	request = urllib2.Request(
		url = url,
		headers = headers
	)

	request.add_header("Cookie", cookie)
	response = urllib2.urlopen(request)

	html = response.read()

	soup = BeautifulSoup(html, 'html.parser')

	# 格式化输出
	# print soup.prettify()

	book = Workbook(encoding='utf-8')
	sheet = book.add_sheet('销售信息')

	rowIndex = 0
	for saleInfo in soup.find_all('div', id=re.compile('\d{16}')):

		# 子节点
		child = saleInfo.find('div')

		columnIndex = 0

		for spanInfo in child.find('div').find_all('span'):
			#print spanInfo.string
			sheet.write(rowIndex, columnIndex, spanInfo.string)
			columnIndex += 1

		sheet.write(rowIndex, columnIndex, child.contents[1])
		columnIndex += 1

		# print child.contents[3]
		sheet.write(rowIndex, columnIndex, child.contents[3])
		
			
		rowIndex += 1	

	# 文件保存
	book.save('1.xls')
	book.save(TemporaryFile())
			
except urllib2.HTTPError, e:
	print e.code
	print e.msg
	print e.headers
	print e.fp.read()
