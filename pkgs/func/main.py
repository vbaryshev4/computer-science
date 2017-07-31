def print_hey():
	"""
		>>> print_hey()
		hey
	"""
	return 'hey'
	

def print_sum(a, b):
	"""
		>>> print_sum(2,2)
		4
	"""

	result = a + b
	return result

def times(func, loops, *args):
	"""
		>>> times(print_sum, 2, 10, 3)
		[13,13]
	"""
	result = []
	for i in range(loops):
		r = (func(*args))
		result.append(r)
	return result


