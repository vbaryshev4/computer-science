from pkgs.calc import * 
from pkgs.tester import *

class CalcTest(Suite):

	module = "pkgs.calc"

	def calc_test(self):
		self.equality_case(
			calc("qwe"), 'qwe',
				"Should return a result of calculation: string case"
		)

		self.equality_case(
			calc("1+2-3"), 0,
				"Should return a result of calculation: integers case"
		)

MainTest = CalcTest()
