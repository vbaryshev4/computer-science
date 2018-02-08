from random import randint


def partirion(lst, fn):
    lst = [[],[]]
    for num in lst:
        if fn(num):
            lst[0].append(num)
        else:
            lst[1].append(num)
    return lst
    
def shuffle(lst):
    lst = lst.copy()
    shuffled_list = []
    while len(lst) != 0:
        elem = randint(0, len(lst) - 1)
        shuffled_list.append(lst[elem])
        lst = lst[:elem] + lst[elem+1:]
    return shuffled_list

def chunk(lst, size):
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

def get_last_item(lst):
    while isinstance(lst[-1], list):
        lst = lst[-1]
        # print(lst)
    return lst[-1]

def traverse_recursive(node, fn):
    if not isinstance(node, list):
        return fn(node)
    else:
        for i in range(len(node)):
            node[i] = traverse_recursive(node[i], fn)
        return node

def flatten_recursive(lst):
    result = []
    if not isinstance(lst, list):
        result.append(lst)
        return result # Final return of this function
    else:
        if len(lst) == 0:
            return []

        return flatten_recursive(
            lst[0]
        ) + flatten_recursive(
            lst[1:]
        ) 

def flatten(lst):
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
    result = []
    for i in lst:
        if i not in items_to_del:
            result.append(i)

    return result

def uniq(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

def map(fn_mapper, lst):
    return [fn_mapper(i) for i in lst]

def filter(fn_predicate, lst):
    return [i for i in lst if fn_predicate(i) == True]

def from_pairs(lst):
    lst_dict = {}
    for i in lst:
        lst_dict.update([i])
    
    return lst_dict

def count(lst):
    result = {}
    for i in lst:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return result

def pick(dctnry, lst):
    result = {}
    for l in lst:
        try:
            result[l] = dctnry[l]
        except KeyError:
            pass            
    return result