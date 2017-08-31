def map(fn_mapper, lst):
    return [fn_mapper(i) for i in lst]

def filter(fn_predicate, lst):
    return [i for i in lst if fn_predicate(i) == True]

users = [
	{
		'username': '@zolgoedr', 
		'password': '123123',
		'age': 12
	},
	{
		'username': '@adsdsds', 
		'password': '5435353',
		'age': 20
	},
	{
		'username': '@redaczxc', 
		'password': 't45354',
		'age': 16
	},
	{
		'username': '@ds344', 
		'password': '302423',
		'age': 29
	}
]

# def get_username(user):
# 	return user.get('username')

# def get_password(user):
# 	return user.get('password')

def get_property(property):

	def getter(_dict):
		return _dict.get(property)
	return getter

def add(a):
	def sum(b):
		return a + b
	return sum

def is_over_18(user):
	return user.get('age') > 18

a = 666
get_property(a)

usernames = map(get_property('username'), users)
passwords = map(get_property('password'), users)

over_18 = filter(is_over_18, users)
over_18_usernames = map(
	get_property('username'),
	filter(is_over_18, users)
)

def over(age):
	def predicate(user):
		return user.get('age') > age
	return predicate

over_21 = filter(over(21), users)

#fn = get_dict_property
#curried_args = ('username')
def curry(fn, *curried_args):
	
	def curried(*args):
		#args = ({'username': '123'})
		arguments = curried_args + args
		# arguments = ('username', {'username': '123'})
		# get_dict_property('username', {'username': '123'})
		res = fn(*arguments)
		return res
	return curried

def get_dict_property(prop, _dict):
	return _dict.get(prop)

get_username = curry(get_dict_property, 'username')
get_password = curry(get_dict_property, 'password')

get_usernames = curry(map, get_username)
get_passwords = curry(map, get_password)

over_18 = curry(filter, over(18))


