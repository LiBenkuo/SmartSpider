# _*_ coding: utf-8 _*_

import math
import matplotlib.pyplot as plt
from xlwt import Workbook
from xlrd import open_workbook, cellname


book = open_workbook('question_info.xls')
sheet = book.sheet_by_index(0)

index = []
total_accepted = []
total_submissions = []
index_Easy = []
total_accepted_Easy = []
total_submissions_Easy = []
index_Medium = []
total_accepted_Medium = []
total_submissions_Medium = []
index_Hard = []
total_accepted_Hard = []
total_submissions_Hard = []

for row_index in range(sheet.nrows):
    try:
        #total_accepted.append(math.ceil(float(sheet.cell(row_index, 2).value) / 10000))
        #total_submissions.append(math.ceil(float(sheet.cell(row_index, 3).value) / 10000))
        total_accepted.append(float(sheet.cell(row_index, 2).value))
        total_submissions.append(float(sheet.cell(row_index, 3).value))
        index.append(row_index)
        
        if sheet.cell(row_index, 4).value == "Easy":
            total_accepted_Easy.append(float(sheet.cell(row_index, 2).value))
            total_submissions_Easy.append(float(sheet.cell(row_index, 3).value))
            index_Easy.append(row_index)

        elif sheet.cell(row_index, 4).value == "Medium":
            total_accepted_Medium.append(float(sheet.cell(row_index, 2).value))
            total_submissions_Medium.append(float(sheet.cell(row_index, 3).value))
            index_Medium.append(row_index)
        elif sheet.cell(row_index, 4).value == "Hard":
            total_accepted_Hard.append(float(sheet.cell(row_index, 2).value))
            total_submissions_Hard.append(float(sheet.cell(row_index, 3).value))
            index_Hard.append(row_index)
        
    except:
        continue

plt.plot(index, total_accepted, "vr", index, total_submissions, "ob")
#plt.plot(index_Easy, total_accepted_Easy, index_Easy, total_submissions_Easy)
#plt.plot(index_Medium, total_accepted_Medium, index_Medium, total_submissions_Medium)
# plt.plot(index_Hard, total_accepted_Hard, index_Hard, total_submissions_Hard)
plt.grid(True)
plt.xlabel('Question Index')
plt.ylabel('Submissions')
plt.title('LeetCode Submit Tendency')
plt.show()
