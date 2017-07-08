#!/usr/local/bin/python3.6

from modules.string import *

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


# --- *4* ---
def get_tree(string):
    priotities = ['+', '-', '/', '*']
    tree = None

    pass
