from chy_frame.utils1.public import *
import json
from chy_frame.utils1.operation_excel import OperationExcel

class OperationJson():
	def __init__(self):
		self.excel=OperationExcel()
	def getReadJson(self):
		with open(data_dir('data','request_data.json'),'r',encoding='utf-8') as f:
			return json.load(f)
	def getJsonValue(self,row):
		return json.dumps(self.getReadJson()[self.excel.get_data(row=row)])


# obj=OperationJson()
# print(obj.getJsonValue(1))