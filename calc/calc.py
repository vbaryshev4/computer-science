from string import trim, index_of

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
# --- *1* ---
    


# --- *2 – GIT* ---

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
    """
    pass

# --- *4* ---
def get_tree(string):
    priotities = ['+', '-', '/', '*']
    tree = None

    pass

# Test cases:
split("2&33 + 33", "+")
split("6 + 3", "-")
split("7+8+3", "+")
split("10112+4444-3", "-")
# get_char("33+33", "+")
# get_char("3+3", "-")
# get_char("3+3+3", "+")
# get_char("3+3-3", "-")
# get_char("", "-")
# get_char("+"," ")





