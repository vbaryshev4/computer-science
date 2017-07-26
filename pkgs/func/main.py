def print_hey():
	print('hey')
	"""
		>>> print_hey()
		hey
	"""

def print_sum(a, b):
	print(a + b)
	"""
		>>> print_sum(2,2)
		4
	"""

def times(func, loops, *args):
	for i in range(loops):
		func(*args)
	"""
		>>> times(print_sum, 2, 10, 3)
		13
		13
	"""


