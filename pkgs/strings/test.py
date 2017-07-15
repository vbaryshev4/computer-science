import sys 

from pkgs.tester import * 
from pkgs.string import *

testfn = "main"

try:
	testfn = sys.argv[1]
except IndexError:
	pass


def _trim():
    equality_case(trim(''), '', 'Should work with empty string')
    equality_case(trim('  a'), 'a', 'Should trim spaces from start of string')
    equality_case(trim('a   '), 'a', 'Should trim spaces from end of string')
    equality_case(trim('   a   '), 'a', 'Should trim spaces from start & end of string')


def _kebab():
    equality_case(kebab_to_snake("kabeab-to-snake"), 'kabeab_to_snake', 'Should change all - to _')
    equality_case(kebab_to_camel("kabeab-to-camel"), 'kabeabToCamel', 'Should return camelCase string')

def _parentes():
    equality_case(parentes("1+(2+3)"), (2, "2+3"), "Should work correctly")
    equality_case(parentes("1+3"), (-1, None), "Should return None if not found")
    error_case(lambda:parentes('('), 'Should raise ValueError on invalid expression')

def _count():
    equality_case(count("(((", "("), (3), "Should work correctly") 
    equality_case(count("+-+++--", "+"), (4), "Should work correctly") 
    equality_case(count("aAaAAA", "a"), (2), "Should work correctly") 
    equality_case(count("?###!%", "?"), (1), "Should work correctly") 
    equality_case(count("?###!%", "#"), (3), "Should work correctly")

def _capitalize():
    equality_case(capitalize('this is my world'),('This Is My World'), "Should work correctly")
    equality_case(capitalize('hello'),('Hello'), "Should work correctly")
    equality_case(capitalize('one \ntwo'),('One \nTwo'), "Should work correctly")

def _parentesize():
    equality_case(parentesize('1 + (3 + 8)'), ('1 + $', '3 + 8'), "Should return set of 2, devided by open bracket")
    equality_case(parentesize('1 + 3'), ('1 + 3', None), "Should return set of 2, devided by open bracket")
    equality_case(parentesize('(b + c)'), ('$', 'b + c'), "Should return set of 2, devided by open bracket")
    error_case(lambda:parentesize('))'), "Should raise ValueError")

def _split_by_first():
    equality_case(split_by_first('a', '+'), False, 'Should return false if not found char')
    equality_case(split_by_first('a + b', '+'), ['+', 'a', 'b'], 'Should work correct with single char')
    equality_case(split_by_first('a + b + c', '+'), ['+', 'a', 'b + c'], 'Should work correct with double char')

def _split_all():
    equality_case(split_all_by_recursive('a', '+'), 'a', 'Should work correct with simple strings')
    equality_case(split_all_by_recursive('a + b', '+'), ['+', 'a', 'b'], 'Should work correct with single char')
    equality_case(split_all_by_recursive('a + b + c', '+'), ['+', 'a', ['+', 'b', 'c']], 'Should work correct with double char')

module = "string module"

blocks = {

	'trim': _trim,
	'kebab': _kebab,
	'parentes': _parentes,
	'count': _count,
	'capitalize': _capitalize,
	'parentesize': _parentesize
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



