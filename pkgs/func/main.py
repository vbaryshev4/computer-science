def print_hey():
	print('hey')
	"""
		>>> print_hey()
		hey
	"""

def print_sum(a, b):
	print(a + b)
	"""
		>>> print_sum_two_times = times(print_sum, 2)
		>>> print_sum(10, 3)
		13
		13
	"""

def times(func, loops, *args):
	for i in range(loops):
		func(*args)
	"""
		>>> times(print_hey, 6)
			'hey'
			'hey'
			'hey'
			'hey'
			'hey'
			'hey'
	"""


