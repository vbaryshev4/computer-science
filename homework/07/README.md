# 07

## Реализация filter и map для dict

Тебе нужно придумать и спроектировать такие же методы как filter и map, но работающие со словарями:

```python

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


over_18 = dict_filter(predicate, users)

# Вернет
# users = {
#     'tim': {
#         'age': 19,
#         'username': '@trooo'
#     },
#     'bob': {
#         'age': 33,
#         'username': '@bibob'
#     }
# }

usernames = dict_map(mapper, users)

# Вернет
# users = {
#     'joe': '@joe',
#     'tim': '@trooo',
#     'bob': '@bibob'
# }
```

## Дополнительные функции


#### once
`once` - функция, которая принимает функцию fn и возвращает функцию, которая вызывает fn не больше одного Реализация

```python
def print_hello():
    print('hello')

```

Использование 

```
>>> print_hello()
>>> 'hello'
>>> print_hello()
>>> 'hello'
>>> print_hello()
>>> 'hello'
```

```python
def once(fn):
    pass # тебе нужно написать эту функцию

print_hello_once = once(print_hello)
```

```
>>> print_hello_once()
>>> 'hello'
>>> print_hello_once() #ничего не происходит
>>> print_hello_once() #ничего не происходит
>>> print_hello_once() #ничего не происходит
```

Функция once как бы ограничивает выполнение функции, которую ей передали и дает ей возможность вызываться только один раз. 

#### negate

Функция `negate` - принимает предикат и возвращает предикат, который является обратным предикатом к данному

```python

def more_than_5(x):
    return x > 5

more_than_5(10) # True

less_or_equal_than_5 = negate(more_than_5)

less_or_equal_than_5(10) # False
less_or_equal_than_5(3) # True
```
