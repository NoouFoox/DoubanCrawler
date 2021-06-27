# -*- coding:utf-8 -*-
# @author: 贺俊浩🐱
# @file: testXwlt.py
# @time: 2021/6/27 19:33

import xlwt

'''
workbook = xlwt.Workbook(encoding="utf-8")  # 创建work对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
worksheet.write(0, 0, 'hello')
workbook.save("s.xls")
'''
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet.write(i, j, "%d×%d=%d" % (i + 1, j + 1, (i + 1) * (j + 1)))
workbook.save("s.xls")
