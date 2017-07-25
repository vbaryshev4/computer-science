from random import randint

"""
**************************
****** List to list* *****
**************************
"""

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
        # print(lst)
    return lst[-1]

def traverse(node, fn):
    """
        >>> traverse([0,[1,[2,3,4]]], print)
            0
            1
            2
            3
            4
            [None, [None, [None, None, None]]]
    """
    if not isinstance(node, list):
        return fn(node)
    else:
        for i in range(len(node)):
            node[i] = traverse(node[i], fn)
        return node


def flatten(lst):
    """
        >>> flatten([1, [2, [3, [4]], 5]]);
        [1, 2, 3, 4, 5]
    """
    result = []
    
    if not isinstance(lst, list):
        result.append(lst) # Append delete each element from the list
        print("Cuted this list") # Signals that element != type(list)     
        return result # Final return of this function
    else:
        if len(lst) == 0:
            return []

        print("List is:",lst, "and result is:", result) # Recursion progress
        return flatten(lst[0]) + flatten(lst[1:]) # Main call of recursion


"""
**************************
****** List to dict* *****
**************************
"""

def from_pairs(lst):
    """
        >>> from_pairs([['a', 1], ['b', 2], ['c', 3]]);
        { 'a': 1, 'b': 2, 'c': 3}

        >>> from_pairs([['a', 1], ['a', 2]]);
        { 'a': 2 }
    """
    lst_dict = {}

    for i in lst:
        lst_dict.update([i])
    
    return lst_dict








