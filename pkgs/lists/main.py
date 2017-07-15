from random import randint

def shuffle(lst):
    """
        Принимает список: lst и перемешивает в нем элементы
        Возвращает другой (!sic) список. Это значит, 
        что исходный список нельзя трогать.
    """
    lst = lst.copy()
    shuffled_list = []

    while len(lst) != 0:
        elem = randint(0, len(lst) - 1)
        shuffled_list.append(lst[elem])
        lst = lst[:elem] + lst[elem+1:]
    return shuffled_list


def chunk(lst, size):
    """ 
        Принимает список - lst и целое число - size
        Возвращает список списков длиной в size, заполненных данными из списка lst
        Пример смотри ниже
    """
    result = []
    a, b = 0, size
    i = 0
    while i < len(lst):
        result.append(lst[a:b])
        i += size
        a += size
        b += size
    return result


def change_last_item(arr, fn):
    last = arr[-1]
    stack = []

    while isinstance(last, list):
        stack.append(last)
        last = last[-1] 

    stack.append(last)    
    stack.reverse()

    prev = None

    for i in stack:
        if not isinstance(i, list):
            prev = fn(i) 
        else:
            i[-1] = prev 
            prev = i

    arr[-1] = prev 
    return arr
