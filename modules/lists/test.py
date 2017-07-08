#!/usr/local/bin/python3.6

import sys
from modules.lists import *
from modules.tester import *

testfn = "main"

try:
	testfn = sys.argv[1]
except IndexError:
	pass


def _shuffle():
	non_equality_case(shuffle([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7], 'Shuffles a list with ints')
	non_equality_case(shuffle(['a','b','c','d']), ['a','b','c','d'], 'Shuffles a list with str')
	non_equality_case(shuffle([1,2,3,'a','b','c']), [1,2,3,'a','b','c'], 'Shuffles a list with mixed')



module = "lists module"

blocks = {
	'shuffle': _shuffle
}

if testfn in blocks:
	blocks[testfn]()
elif testfn == "main":
	for i in blocks:
		print(i)
		blocks[i]()
		print('\n\n')
else:
	print("----")
	print("No function: %s in %s" % (testfn, module))


