#!/usr/local/bin/python3.6

# check module
def case_generator(checking_func, error_msg):

	def case(real, expected, msg):
		print("---- ")
		print("Message: " + msg)

		if checking_func(real, expected):
			print('Status: OK')
		else:
			print('Status Fail: ' + error_msg.format(real, expected))

	return case

# checking_func
def exists(real, expected):
	return real != None

def equals(real, expected):
	return real == expected

def not_equals(real, expected):
	return real != expected

def is_empty(real, expected):
	return len(real) == 0

def value_to_types(real, expected):
	return type(real) == expected

def types_to_types(real, expected):
	return type(real) == type(expected)

def lenght_list(real, expected):
	return len(real) >= len(expected) 

none_case = case_generator(exists, '{0} is None')
equality_case = case_generator(equals, '{0} was given and {1} expected')
non_equality_case = case_generator(not_equals, '{0} was given and {1} was not expected')
empty_case = case_generator(is_empty, '{0} not empty')
type_case = case_generator(value_to_types, '{0} type is not {1}')
same_type_case = case_generator(types_to_types,'Type of {0} should be same type as type of {1}')
shorter_case = case_generator(lenght_list, 'List of {0} shorter than list of {1}')

def error_case(fn, case):
	print("---- ")
	print("Message: " + case)
	try:
		fn()
		print('Status Fail: expected error')
	except:
		print('Status: Ok')
