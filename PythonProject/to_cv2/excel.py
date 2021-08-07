import matplotlib.pyplot as plt
import sys
from xlrd import open_workbook

input_file = '判断题5.xlsx'
fo = open("概论判断题.txt", "a")
list1 = ['序号:', '', '答案:']
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_index(0)
    for row_index in range(worksheet.nrows):
        for column_index in range(3):
            fo.write(list1[column_index] + str(worksheet.cell_value(row_index, column_index)) + '\n')
        fo.write('\n')
fo.close()