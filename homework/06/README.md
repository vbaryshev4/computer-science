# 06

## Области видимости

Что произойдет если выполнить следующий код? Почему? 

1.
```python
a = 10

def fn():
    print(a)
    a = 20

fn()
```

2.
```python
a = 10

def fn():
    a = 20
    print(a)

fn()
print(a)
```

3. 
```python
a = 10

def fn():
    global a
    a = 20
    print(a)

fn()
print(a)
```

## Замыкания

1. Что такое замыкание?

2. Что произойдет если выполнить этот код
```python
def fn1(a):
    def fn2():
        return a
    a += 10
    return fn2

f = fn1(10)
f() 
```

2. Как пользоваться этим замыканием, что оно делает?
```python
def closure(a):
    def fn(b):
        return a + b

add10 = closure(10)
```

## Функции высшего порядка

Для начала допустим у нас есть список пользователей следующего вида:

```
data = [
    {
        'age': <Int>,
        'name': <String>,
        'username': <String>,
    },
    ...
]


## Фильтрация

Предположим, что нам нужно написать функцию-фильтр. Это такая функция, которая фильтрует данный список по функции-предикату. Функция-предикат, это такая функция которая возвращает True или False. Например: 

```python
def is_user_over_18(user):
    return user.get('age') > 18
```

Такой предикат возвращает True, если у данного аргумента свойство `'age'` больше 18

Теперь напишем `filter`:

```python
def filter(predicate, fn):
    pass

users_over_18 = filter(is_user_over_18, data)  #список всех пользователей старше 18
```

## Преобразование



```python
def to_lower_username(user):
    user['username'] = lower(user.get('username'))
    return user


def map(mapper, fn):
    pass

to_lower_usernames = map(to_lower_usernames, data) 
```
