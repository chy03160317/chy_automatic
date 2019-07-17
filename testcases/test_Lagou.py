import unittest
from chy_frame.base.method import Method

class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
	def test_lagou_001(self):
		r=self.obj.post(1)
		print(r.text)

if __name__ == '__main__':
	unittest.main(verbosity=2)
