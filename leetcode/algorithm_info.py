# -*- coding: utf-8 -*-

import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from xlwt import Workbook
from xlrd import open_workbook, cellname

driver = webdriver.Firefox()
domainName = "https://leetcode.com/"

book = open_workbook('leetcode.xls')
sheet = book.sheet_by_index(0)

wb = Workbook()
wbs = wb.add_sheet('question info')

row = 1

for row_index in range(sheet.nrows):
    if sheet.cell(row_index, 5).value == 'lock':
        continue

    #time.sleep()
    col = 1
    
    path = sheet.cell(row_index, 4).value
    if path is None or path == '':
        row = row + 1
        continue
    
    wbs.write(row, col, path)
    col = col + 1

    index = 0
    driver.get(domainName + path)
    try:
        infos = driver.find_element_by_class_name('question-info')
    except selenium.common.exceptions.NoSuchElementException:
        index = index + 1
        print "Need Login {0:5d}".format(index)
        row = row + 1
        continue

    soup = BeautifulSoup(infos.get_attribute('innerHTML'), 'html.parser')
    
    for li in soup.find('ul').find_all('li'):
        wbs.write(row, col, li.find('strong').text)
        col = col + 1
    row = row + 1

wb.save('question_info.xls')
driver.close()
