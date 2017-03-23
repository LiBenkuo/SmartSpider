# _*_ coding: utf-8 _*_

import math
import matplotlib.pyplot as plt
from xlrd import open_workbook, cellname

book = open_workbook("leetcode.xls")
sheet = book.sheet_by_index(0)

index = []
acceptances = []

for row_index in range(sheet.nrows):
    try:
        #acceptances.append(math.ceil(float(sheet.cell(row_index, 7).value.strip('%')) / 10))
        acceptances.append(float(sheet.cell(row_index, 7).value.strip('%')))
        index.append(row_index)
    except:
        continue

plt.plot(index, acceptances, "ob")
plt.grid(True)
plt.xlabel('Question Index')
plt.ylabel('Acceptance')
plt.title('Acceptance Tendency')
plt.show()
