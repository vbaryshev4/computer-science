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

def times(func, num):
	"""
	>>> print_sum_two_times = times(print_sum, 2)
	>>> print_hey_six_times(10, 3)
	13
	13
	"""
	def result(*args):
		t = num
		while t:
			func(*args)
			t -= 1

	return result

