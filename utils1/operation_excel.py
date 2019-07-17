import xlrd
from xlutils.copy import copy
from chy_frame.utils1.public import *
'''有时候自定义的模块导入不成功，那就尝试把上级模块也导入'''

from chy_frame.utils1.excel_colums import *



class OperationExcel:
	def get_excel(self):
		excel=xlrd.open_workbook(data_dir('data','data.xls'))
		sheet=excel.sheet_by_index(0)
		return sheet
	def get_excel_rows(self):
		return self.get_excel().nrows
	def get_row_col(self,row,col):
		return self.get_excel().cell_value(row,col)
	def get_url(self,row):
		return self.get_row_col(row,getUrl())
	def get_data(self,row):
		return self.get_row_col(row,getRequestData())
	def get_expect_result(self,row):
		return self.get_row_col(row,getExpectResult())
	def get_actual_result(self,row):
		return self.get_row_col(row,getActualResult())


# obj=OperationExcel()
# print(obj.get_data(1))

