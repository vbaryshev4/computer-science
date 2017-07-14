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

# chunk(list(range(10)), 2)
# [[0, 1], [2, 3], [4, 5], [5, 6], [7, 8], [9]]

# chunk(list(range(10)), 3)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
# chunk(list(range(10)), 7)
# [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]]

def change_last_item(arr, fn):
    # ['a', ['c', 'd', ['e']]]    
    last = arr[-1] #['c', 'd', ['e']]
    stack = []

    # 1. [ ['c', 'd', ['e']] ]
    # 2. [ ['c', 'd', ['e']], ['e'] ]
    while isinstance(last, list):
        stack.append(last)
        last = last[-1] 

    stack.append(last)
    
    # 3. [ ['c', 'd', ['e']], ['e'], 'e' ]
    
    stack.reverse()

    # reverse: ['e', ['e'], ['c', 'd', ['e']]]
    print('stack:', stack)

    prev = None


    for i in stack:
        # 1. i = 'e'
        # 2. i = ['e']
        # 3. i = ['c', 'd', ['e']]
        if not isinstance(i, list):
            prev = fn(i) 
        else:
            i[-1] = prev 
            prev = i # prev = ['c', 'd', ['E']]

    arr[-1] = prev 
    return arr



