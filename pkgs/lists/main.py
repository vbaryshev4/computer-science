from random import randint

def shuffle(lst):
    """
        >>> shuffle(['a','b','c'])
        ['c', 'b', 'a']
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
        >>> chunk(list(range(10)), 7)
        [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]]
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
    """
        >>> change_last_item([1,2,3], print)
        3
        [1, 2, None]
    """
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

def get_last_item(lst):
    """
        >>> get_last_item([0,1,2])
        2
        >>> get_last_item([0,[1,[2]]])
        2
        >>> get_last_item([0,[1,[2,3,4]]])
        4
    """
    while isinstance(lst[-1], list):
        lst = lst[-1]
    return lst[-1]


