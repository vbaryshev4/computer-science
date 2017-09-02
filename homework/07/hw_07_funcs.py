users = {
    'joe': {
        'age': 12,
        'username': '@joe'
    },
    'tim': {
        'age': 19,
        'username': '@trooo'
    },
    'bob': {
        'age': 33,
        'username': '@bibob'
    }
}

## Реализация filter и map для dict
# Придумать и спроектировать filter и map, но работающие со словарями.


def get_property(property):
    def getter(_dict):
        return _dict.get(property)
    return getter
    
def dict_map(fn_mapper, dctnry):
    new_dict = {}
    for i in dctnry:
        user_dict = fn_mapper(dctnry[i])
        new_dict.update({i:user_dict})
    return new_dict


usernames = dict_map(get_property('username'), users)
print(usernames)
'''
users = {'joe': '@joe','tim': '@trooo','bob': '@bibob'}
'''

def over(age):
    def predicate(user):
        return user.get('age') > age
    return predicate

def dict_filter(fn_predicate, dctnry):
    new_dict = {}
    for i in dctnry:
        if fn_predicate(dctnry[i]) == True:
            new_dict.update({i:dctnry[i]})
    return new_dict
        # [i for i in lst if fn_predicate(i) == True]


over_18 = dict_filter(over(18), users)
print(over_18)
'''
users = {'tim': {'age': 19,'username': '@trooo'},'bob': {'age': 33,'username': '@bibob'}}
'''

#### once

#`once` - функция, которая принимает функцию fn 
# и возвращает функцию, которая вызывает fn не больше одного

def print_hello():
    print('hello')

'''
>>> print_hello()
>>> 'hello'
>>> print_hello()
>>> 'hello'
>>> print_hello()
>>> 'hello'
'''

# Задача: написать эту функцию
def once(fn):
    c = 0
    while c != 2:
        c += 1
        return fn()
    return -1

print_hello_once = once(print_hello)


'''
>>> 'hello'
>>> print_hello_once #ничего не происходит
>>> print_hello_once #ничего не происходит
>>> print_hello_once #ничего не происходит
'''

# Функция once как бы ограничивает выполнение функции, 
# которую ей передали и дает ей возможность вызываться только один раз.

##!! – ограничивает выполнение функции в рамаках работы python -i ???? 
##!! или при перезагрузке программы она не должна больше работать ????

#### negate

# Функция `negate` - принимает предикат и возвращает предикат, 
# который является обратным предикатом к данному

def more_than_5(x):
    return x >= 5

def negate(fn):
    return fn

# data = more_than_5(10) # True
# print(data)

less_or_equal_than_5 = negate(more_than_5(10))
print(less_or_equal_than_5) # True

less_or_equal_than_5 = negate(more_than_5(5))
print(less_or_equal_than_5) # True

less_or_equal_than_5 = negate(more_than_5(3))
print(less_or_equal_than_5) # True




