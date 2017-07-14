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

def eval(tree):
    if not isinstance(tree, list):
        return tree

    fn = fns[tree[0]]
    left = tree[1]
    right = tree[2]

    return fn(eval(left), eval(right))

def get_tree(string):
    priotities = ['+', '-', '/', '*']
    tree = None
    pass

