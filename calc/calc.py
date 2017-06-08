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
    
def split(string, char):
    """
        Принимает строку и символ, возвращает:
         - [char, part1, part2] если символ есть в строке
         - False - если символа в строке нет
        Внимание: функция стрипит пробелы у part1 part2
        Exmaple:
         - split('2 + 3', '+') = ['+', '2', '3']
         - split('2 + 3', '-') = False
    """
    def strip_string(string):
        no_spaces = string.replace(" ", "")
        return no_spaces

    def get_char_index(string, char):
        char_index = None
        if string.find(char) == -1:
            return False
        else:
            char_index = (string.find(char))
            return char_index

    def get_left_part(string, index):
        part_1 = ''
        if type(index) == int:
            for i in range(0, index):
                if string[i].isdigit():
                    part_1 += string[i]
                else:
                    part_1 = ''
        return part_1

    def get_right_part(string, index):
        part_2 = ''
        if type(index) == int:
            for i in range(index, len(string)):
                if string[i].isdigit():
                    part_2 += string[i]
                else:
                    part_2 = ''
        return part_2       

    result = []
    string = strip_string(string)
    index = get_char_index(string, char)
    part1 = get_left_part(string, index)
    part2 = get_right_part(string, index)

    if index == False:
        return False
    else:
        result.append(string[index])
        result.append(part1)
        result.append(part2)
    pass
    # print(result)
    return result
    

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





