#!/usr/local/bin/python3.6


from modules.string import *
from modules.tester import *
 
equality_case(trim('  a'), 'a', 'Should trim spaces from start of string')
equality_case(trim('a   '), 'a', 'Should trim spaces from end of string')

equality_case(kebabToSnake("kabeab-to-snake"), 'kabeab_to_snake', 'Should change all - to _')
equality_case(kebabToCamel("kabeab-to-camel"), 'kabeabToCamel', 'Should return camelCase string')

equality_case(parentes("1+(2+3)"), (2, "2+3"), "Should return first ( and inside values")
equality_case(parentes("1+3"), None, "Should return None if not found")
error_case(lambda:parentes('('), 'Should raise ValueError on invalid expression')

equality_case(count("(((", "("), (3), "Should count symbols correctly") 
equality_case(count("+-+++--", "+"), (4), "Should count symbols correctly") 
equality_case(count("aAaAAA", "a"), (2), "Should count symbols correctly") 
equality_case(count("?###!%", "?"), (1), "Should count symbols correctly") 
equality_case(count("?###!%", "#"), (3), "Should count symbols correctly")

equality_case(capitalize('this is my world'),('This Is My World'), "Should capitalize all first letters")
equality_case(capitalize('hello'),('Hello'), "Should capitalize all first letters")
equality_case(capitalize('one \ntwo'),('One \nTwo'), "Should capitalize all first letters")

equality_case(parentesize('1 + (3 + 8)'), ('1 + $', '3 + 8'), "Should return set of 2, devided by open bracket")
equality_case(parentesize('1 + 3'), ('1 + 3', None), "Should return set of 2, devided by open bracket")
equality_case(parentesize('(b + c)'), ('$', 'b + c'), "Should return set of 2, devided by open bracket")

# Починить не смог.
# def _trim():
# 	equality_case(trim('  a'), 'a', 'Should trim spaces from start of string')
# 	equality_case(trim('a   '), 'a', 'Should trim spaces from end of string')

# def _kebab():
# 	equality_case(kebabToSnake("kabeab-to-snake"), 'kabeab_to_snake', 'Should change all - to _')
# 	equality_case(kebabToCamel("kabeab-to-camel"), 'kabeabToCamel', 'Should return camelCase string')

# def _parentes():
# 	equality_case(parentes("1+(2+3)"), (2, "2+3"), "Should work correctly")
# 	equality_case(parentes("1+3"), None, "Should return None if not found")
# 	error_case(lambda:parentes('('), 'Should raise ValueError on invalid expression')

# def _count():
# 	equality_case(count("(((", "("), (3), "Should work correctly") 
# 	equality_case(count("+-+++--", "+"), (4), "Should work correctly") 
# 	equality_case(count("aAaAAA", "a"), (2), "Should work correctly") 
# 	equality_case(count("?###!%", "?"), (1), "Should work correctly") 
# 	equality_case(count("?###!%", "#"), (3), "Should work correctly")

# def _capitalize():
# 	equality_case(capitalize('this is my world'),('This Is My World'), "Should work correctly")
# 	equality_case(capitalize('hello'),('Hello'), "Should work correctly")
# 	equality_case(capitalize('one \ntwo'),('One \nTwo'), "Should work correctly")

# blocks = {
# 	'trim': _trim,
# 	'kebab': _kebab,
# 	'parentes': _parentes,
# 	'count': _count,
# 	'capitalize': _capitalize
# }

# if testfn == 'main':
# 	for i in blocks:
# 		print(i)
# 		blocks[i]()
# 		print('\n\n')
# else:
# 	if blocks.get(testfn):
# 		print(testfn)
# 		blocks[testfn]()
# 	else:
# 		print('No function {}'.format(testfn))


