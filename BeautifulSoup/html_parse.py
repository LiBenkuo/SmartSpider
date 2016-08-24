# -*- coding: utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

from tempfile import TemporaryFile
from xlwt import Workbook

try:

	url = "http://www.gyfc.net.cn/pro_query/index/floorView.aspx?dongID=16009890&danyuan=(C1)1&qu=清镇&yszh=2014002"
	#url = "http://www.gyfc.net.cn/pro_query/FloorList.aspx?yszh=2014002&qu=6"

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
	for saleInfo in soup.find_all('div', class_=re.compile('P0 W[2,3] H0')):
		roomCode = saleInfo.find('span').string

		columnIndex = 0
		sheet.write(rowIndex, columnIndex, roomCode)
		for i in saleInfo['title'].split():
			columnIndex += 1
			sheet.write(rowIndex, columnIndex, i)
			
		rowIndex += 1	

	# 文件保存
	book.save('统计信息.xls')
	book.save(TemporaryFile())
			
except urllib2.HTTPError, e:
	print e.code
	print e.msg
	print e.headers
	print e.fp.read()
