from modules.lists import *
from modules.tester.cases import *
from modules.tester import Suite

class ListTests(Suite):
	def shuffle_test(self):
		non_equality_case(shuffle([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7], 'Shuffles a list with ints')
		non_equality_case(shuffle(['a','b','c','d']), ['a','b','c','d'], 'Shuffles a list with str')
		non_equality_case(shuffle([1,2,3,'a','b','c']), [1,2,3,'a','b','c'], 'Shuffles a list with mixed')
