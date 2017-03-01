# -*- coding: utf-8 -*-

import urllib2
import re
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from tempfile import TemporaryFile
from xlwt import Workbook

try:
    driver = webdriver.Firefox()
    url = "https://leetcode.com/problemset/algorithms/"
    driver.get(url)

    select = Select(driver.find_element_by_xpath("//span[@class='row-selector']/select[1]"))
    select.select_by_index(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    

    container = soup.find('div', class_='container')
    
    rows = soup.findAll('tr')
    
    book = Workbook()
    sheet1 = book.add_sheet('Sheet 1')
    
    rowNum = 1
    for tr in rows:
        cols = tr.findAll('td')
        colNum = 1
        for td in cols:
            sheet1.write(rowNum, colNum, td.text)
            colNum = colNum + 1
            
            if td.find('div') is not None:
                sheet1.write(rowNum, colNum, td.find('div').find('a').get('href'))
                colNum = colNum + 1
            
                if td.find('div').find('i') is not None:
                    sheet1.write(rowNum, colNum, 'lock')
                else:
                    sheet1.write(rowNum, colNum, 'unlock')
                colNum = colNum + 1
                    
        rowNum = rowNum + 1
    
    driver.close()
    book.save('leetcode.xls')
    
except urllib2.HTTPError, e:
    print e.code
    print e.msg
    print e.headers
    print e.e.fp.read()

