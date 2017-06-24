import sys
sys.path.insert(0, '/Users/vbaryshev/Documents/Python files/Trdat/computer-science')

from string.string import *

fns = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

def calc(expression):
    tree = get_tree(expression)
    result = eval(tree)
    return result


# ['+', 3, ['*', 4, 2]]
def eval(tree):
    if not isinstance(tree, list):
        return tree

    fn = fns[tree[0]]
    left = tree[1]
    right = tree[2]

    return fn(eval(left), eval(right))

#Домашнее задание:
# --- *3* ---
def split_all_by(string, char):
    """
        Принимает строку-выражение и символ по которому
        нужно разбить строку на списки
        Внимание: исходные списки не должны содержать символ по
        которому происходит разбиение
        Example:
         - split_all_by('3 + 2 + 6', '+') -> ['+', '3', ['+', '2', '6']]
         - split_all_by('3 - 6 + 2', '-') -> ['-', '3', '6 + 2']
         - split_all_by('3 + 9', '*') -> '3 + 9' 

        Нужно использовать уже готовый split
    """
    pass

# --- *3.1* ---
'''
    Оценить функции ассемтотически
'''

# --- *4* ---
def get_tree(string):
    priotities = ['+', '-', '/', '*']
    tree = None

    pass
