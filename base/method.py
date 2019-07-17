import requests
from chy_frame.utils1.excel_colums import *
from chy_frame.utils1.operation_excel import OperationExcel
from chy_frame.utils1.operation_json import OperationJson

class Method():
	def __init__(self):
		self.excel=OperationExcel()
		self.json=OperationJson()
	def post(self,row):
		try:
			r=requests.post(
				url=self.excel.get_url(row=row),
				data=self.json.getJsonValue(row=row),
				headers=getLagouHeader(),
				timeout=6)
			return r
		except Exception as e:
			raise RuntimeError('接口请求发生未知错误')
