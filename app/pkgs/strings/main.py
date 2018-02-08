from pkgs.lists import change_last_item, get_last_item, traverse_recursive


def index_of(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

def count(string, char):
    count_of = 0
    for i in string:
        if i == char:
            count_of += 1
    return count_of

def substring(string, sub, start = 0):
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

def trim(string, char = ' '):
    if string == "":
        return string
    while string[0] == char:
        string = string[1:]
    while string[-1] == char:
        string = string[:-1]
    return string

def split_by_first(string, char):
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
    result = split_by_first(string, char) 
    if result:
        result[2] = split_all_by(result[2], char)
        return result
    else:
        return string

def split_all_by(string, char):
    result = split_by_first(string, char) 
    if not result:
        return string
    last_item = result[-1]
    while index_of(last_item, char) != -1:
        result = change_last_item(result, lambda str:split_by_first(str, char))
        last_item = get_last_item(result)
    return result

def replace(string, char, new_char):
    while index_of(string, char) != -1:
        index = index_of(string, char)
        string = (string[:index] + new_char + string[index+1:])
    return string

def kebab_to_snake(string):
    string = replace(string, "-", "_")
    return string

def kebab_to_camel(string):
    while index_of(string, "-") != -1:
        index = index_of(string, "-")
        string = (string[:index] + string[index+1].upper() + string[index+2:])
    return string

def capitalize(string):
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

def interpolate(string, data = {}):
    for key in data:
        string = string.replace('{' + key + '}', data[key])
    return string

def full_replace(string, tpl, change):
    s = substring(string, tpl)
    while s != -1 and s <= len(string):
        string = string[:s] + change + string[s + len(tpl):]
        s = substring(string, tpl, s+len(change))
    return string

def parse(string): 
    symbols = ['+', '-', '*', '/']
    for symb in symbols:
        def fn(node):
            if node in symbols:
                return node
            result = split_all_by(node, symb)
            return result
        string = traverse_recursive(string, fn)
    
    def str_to_int(node):
        if node.isdigit():
            node = int(node)
        return node
    string = traverse_recursive(string, str_to_int)
    return string