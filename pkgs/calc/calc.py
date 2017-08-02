from pkgs.strings import parse

fns = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

def calc(expression):
    """
        >>> calc("qwe")
        'qwe'

        >>> calc("1+2-3")
        0
    """
    tree = parse(expression)
    result = eval(tree)
    return result

def eval(tree):
    """
        >>> eval(4+2-2)
        4
    """
    if not isinstance(tree, list):
        return tree

    fn = fns[tree[0]]
    left = tree[1]
    right = tree[2]

    return fn(eval(left), eval(right))


