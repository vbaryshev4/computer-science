from random import randint

"""
**************************
**** Transform a list ****
**************************
"""

def partirion(lst, fn):
    lst = [[],[]]
    for num in lst:
        if fn(num):
            lst[0].append(num)
        else:
            lst[1].append(num)

    return lst

def even(i):
    return not i % 2

def odd(i):
    return i % 2
    
nums = [1,2,3,4,5,6,7,8,9,10]
print(partirion(nums, odd))
print(partirion(nums, even))


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

def traverse_recursive(node, fn):
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
            node[i] = traverse_recursive(node[i], fn)
        return node


def flatten_recursive(lst):
    """
        >>> flatten([1, [2, [3, [4]], 5]]);
        [1, 2, 3, 4, 5]
    """
    result = []
    
    if not isinstance(lst, list):
        result.append(lst) # Append delete element from the list
        print("Cuted this list") # Signals that element != type(list)     
        return result # Final return of this function
    else:
        if len(lst) == 0:
            return []

        print("List is:",lst, "and result is:", result) # Recursion progress
        return flatten_recursive(
            lst[0]
        ) + flatten_recursive(
            lst[1:]
        ) # Main call of recursion

def flatten(lst):
    """
        >>> flatten([1, [2, [3, [4]], 5]]);
        [1, 2, 3, 4, 5]
    """
    result = []
    stack = []
    
    while lst != []:
        stack.append(lst[0])
        lst = lst[1:]

        while stack != []:
            item = stack[0]
            if not isinstance(item, list):
                result.append(item)
                stack = stack[1:]
            else:
                stack = item + stack[1:]

    return result


def drop(lst, items_to_del):
    """
        >>> drop([1, 2, 3, 1, 2, 3, 1, 2, 3], [2, 3]);
        [1, 1, 1]

        >>> drop([1, 2, 3, 1, 2, 3, 1, 2, 3], [1]);
        [2, 3, 2, 3, 2, 3]
    """
    result = []
    for i in lst:
        if i not in items_to_del:
            result.append(i)

    return result

def uniq(lst):
    """
        >>> uniq([1, 2, 5, 2, 3, 3])
        [1, 2, 5, 3]

        >>> uniq(['a', 'b', 'c', 'd', 'd', 'a', 'a'])
        ['a', 'b', 'c', 'd']
    """
    # result = set(lst)
    # return list(result)
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

def map(fn_mapper, lst):
    return [fn_mapper(i) for i in lst]

def filter(fn_predicate, lst):
    return [i for i in lst if fn_predicate(i) == True]



"""
**************************
* Transform list to dict * 
**************************
"""

def from_pairs(lst):
    """
        >>> from_pairs([['a', 1], ['b', 2], ['c', 3]]);
        { 'a': 1, 'b': 2, 'c': 3}

        >>> from_pairs([['a', 1], ['a', 2]]);
        { 'a': 2 }

        >>> from_pairs([['a', 2], ['a', 1]])
        {'a': 1}
    """
    lst_dict = {}

    for i in lst:
        lst_dict.update([i])
    
    return lst_dict

def count(lst):
    """
        >>> count(['a', 'a', 'b'])
        {'a': 2, 'b': 1}

        >>> count([1, 2, 3, 2, 3, 3])
        {'1': 1, '2': 2, '3': 3}

        >>> count(['hey', 'hey', 'guis'])
        {'hey': 2, 'guis': 1}
    """
    result = {}
    for i in lst:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return result


def pick(dctnry, lst):
    """
        >>> pick({'a': 10, 'b': 20}, ['a'])
        {'a': 10}

        >>> pick({'a': 10, 'b': 20, 'c': 30, 'd': 40}, ['a', 'd'])
        {'a': 10, 'd': 40}
    """
    result = {}

    for l in lst:
        try:
            result[l] = dctnry[l]
        except KeyError:
            pass            

    return result