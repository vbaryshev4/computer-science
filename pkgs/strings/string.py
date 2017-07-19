from pkgs.lists import change_last_item, get_last_item, traverse

"""
**************************
***** Информационные *****
**************************
"""

def index_of(string, char):
    """
        >>> index_of(" qwe rty", "y")
        7
    """
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

def parentes(string, brackets = ['(', ')']):
    """
        >>> parentes('1 + (3 + 8)')
        (4, '3 + 8')
    """
    index = 0
    index_of_open_parentes = None

    opener, closer = brackets

    open_parentes = count(string, opener)
    closing_parentes = count(string, closer)

    if open_parentes != closing_parentes:
        raise ValueError('Invalid math expression: ' + string)

    while index < len(string):
        if string[index] == opener:
            index_of_open_parentes = index
        elif string[index] == closer:
            return index_of_open_parentes, string[index_of_open_parentes+1:index]
        index += 1
    return  -1, None


def count(string, char):
    """
        >>> count("qwe rty qwe rty", "q")
        2
    """
    count_of = 0
    for i in string:
        if i == char:
            count_of += 1
    return count_of

def substring(string, sub, start = 0):
    """
        >>> substring("qwe rty", "e")
        2
    """

    d = 0
    if len(sub) > len(string):
        return -1

    i = start
  
    while i < len(string):
        letter = string[i]

        if letter == sub[0]:
            j = 1
            while j < len(sub):
                d += 1        
                try:
                    if sub[j] != string[i + j]:
                        break
                except:
                    break
                j += 1
            if j == len(sub):
                return i
        i += 1

        if len(sub) > len(string) - i:
            return -1

    return -1

"""
*************************
***** Преобразующие *****
*************************
"""
def trim(string):
    """
        >>> trim(" qwe ")
        'qwe'
    """
    if string == "":
        return string

    while string[0] == " ":
        string = string[1:]

    while string[-1] == " ":
        string = string[:-1]

    return string


def split_by_first(string, char):
    """
        >>> split_by_first('2 + 3', '+')
        ['+', '2', '3']
    """
    index = index_of(string, char)

    if index != -1:
        return [
            char,
            trim(string[:index]),
            trim(string[index+1:])
        ]
    else:
        return False

def split_all_by_recursive(string, char):
    """
        >>> split_all_by_recursive('3 + 2 + 6', '+')
        ['+', '3', ['+', '2', '6']]
    """
    result = split_by_first(string, char) 
    
    if result:
        result[2] = split_all_by(result[2], char)
        return result
    else:
        return string

def split_all_by(string, char):
    """
        >>> split_all_by('3 + 2 + 6', '+')
        ['+', '3', ['+', '2', '6']]
    """
    result = split_by_first(string, char) 
    # ['+', '2', '3']

    if not result:
        return string

    last_item = result[-1]

    while index_of(last_item, char) != -1:
        result = change_last_item(result, lambda str:split_by_first(str, char))
        last_item = get_last_item(result)

    return result

def replace(string, char, new_char):
    """
        >>> replace(" qwe rty ", "q", "Q")
        ' Qwe rty '
    """
    while index_of(string, char) != -1:
        index = index_of(string, char)
        string = (string[:index] + new_char + string[index+1:])
    return string

def kebab_to_snake(string):
    """
        >>> kebab_to_snake("qwe-rty")
        'qwe_rty'
    """
    string = replace(string, "-", "_")
    return string

def kebab_to_camel(string):
    """
        >>> kebab_to_camel("qwe-rty")
        'qweRty'
    """
    while index_of(string, "-") != -1:
        index = index_of(string, "-")
        string = (string[:index] + string[index+1].upper() + string[index+2:])
    return string


def capitalize(string):
    """
        >>> capitalize("this is my world")
        'This Is My World'
    """
    string = list(string)
    flag = 0
    spacers = [' ', '\n', '\t']

    for i in range(len(string)):
        letter = string[i]

        if letter not in spacers and flag == 0:
            string[i] = letter.upper()
            flag += 1
            continue
        elif letter in spacers:
            flag = 0

    return ''.join(string)


def parentesize(string, value = '$', brackets = ['(', ')']):
    """
        >>> parentesize('1 + (3 + 8)')
        ('1 + $', '3 + 8')
    """
    index, sub_string = parentes(string, brackets)
    if sub_string == None:
        return string, None

    result = string[:index] + value + string[index + len(sub_string)+2:]
    return result, sub_string


def interpolate(string, data = {}):
    """
        >>> interpolate('{a} {b}', {'a': 'Hello','b': 'World'})
        'Hello World'

        >>> interpolate('{one} + {two} = 3', {'one': '1','two': '2'})
        '1 + 2 = 3'
    """
    for key in data:
        string = string.replace('{' + key + '}', data[key])
    return string


def full_replace(string, tpl, change):
    """
        >>> full_replace("qwe rty", "qwe", "rty")
        'rty rty'

    """
    s = substring(string, tpl)
    while s != -1 and s <= len(string):
        string = string[:s] + change + string[s + len(tpl):]
        s = substring(string, tpl, s+len(change))
    return string

def parse(string): 
    """
        >>> parse('1 + 2 - 3 * 4')
        ['+', '1', ['-', '2', ['*', '3', '4']]]
    """
    symbols = ['+', '-', '*', '/']

    for symb in symbols:
        def fn(node):
            if node in symbols:
                return node
            result = split_all_by(node, symb)
            return result
        string = traverse(string, fn)
    
    def str_to_int(node):
        if node.isdigit():
            node = int(node)
        return node

    string = traverse(string, str_to_int)

    return string


