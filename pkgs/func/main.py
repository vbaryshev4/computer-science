def log(fn):
	def logged_fn(*args):
		print(args)
		return fn(*args)
	return logged_fn