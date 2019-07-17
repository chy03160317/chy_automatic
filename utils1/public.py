import os
def data_dir(path=None,file=None):
	'''查找文件目录'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),path,file)

