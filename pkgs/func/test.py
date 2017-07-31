from pkgs.func import * 
from pkgs.tester import *

class FuncTest(Suite):

	module = "pkgs.func"

	def times_test(self):
		equality_case(
			times(print_sum, 1, 10, 3), [13], 
				'Print a sum of args one time'
		)
		equality_case(
			times(print_sum, 4, 10, 3), [13, 13, 13, 13], 
				'Print a sum of args four time'
		)
		equality_case(
			times(print_sum, 0, 10, 3), [], 
				'Print a sum of args zero time'
		)

