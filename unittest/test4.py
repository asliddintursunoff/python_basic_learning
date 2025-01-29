import unittest
import main
class Testing(unittest.TetsCase):
	def expression(self):
		param = 3
		result = main.multiply(param)
		self.AsserEqual(result ,15)

if __name__ == "__main__":
	unittest.main()
