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
'''
users = {'joe': '@joe','tim': '@trooo','bob': '@bibob'}
'''
print(usernames)

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
'''
users = {'tim': {'age': 19,'username': '@trooo'},'bob': {'age': 33,'username': '@bibob'}}
'''
print(over_18)
