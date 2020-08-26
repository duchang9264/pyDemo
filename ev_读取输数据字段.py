from numba import jit
import numpy as np
import xlrd
from datetime import datetime

from xlrd import xldate_as_tuple

data = xlrd.open_workbook('刷数据.xlsx')
table = data.sheets()[0]
# print(table)
# nrows = table.nrows #行数
# ncols = table.ncols #列数
# c1=arange(0,nrows,1)
# print(c1)

start = 833  # 开始的行
end = 10971  # 结束的行

rows = end - start

list_values = []
for x in range(start, end):

    values = {}
    # 读取每行的数据
    row = table.row_values(x)
    # print(value)
    #提取指定列的数值
    values['shopSeq'] = int(row[2]) #网点编号
    values['supplier_name'] = row[5]  # 代理商名字 后期用 != ''
    values['agency_amount'] = row[6]  # 代理费 后期用 != ''

    print('++++' + row[7])
    print('++++' + str(row[2]) + str(type(row[7])))
    if type(row[7]) is float:
        values['contract_begin_time'] = datetime(*xldate_as_tuple(row[7], 0 )).strftime('%Y-%d-%m') # 合同起始日期 后期用 != ''
        values['contract_end_time'] = datetime(*xldate_as_tuple(row[8], 0 )).strftime('%Y-%d-%m')     # 合同结束日期 后期用 != ''
    list_values.append(values)
# print(list_values)
datamatrix = np.array(list_values)
for i in range(len(datamatrix)):
    print(datamatrix[i])
# -*- coding:utf-8 -*-