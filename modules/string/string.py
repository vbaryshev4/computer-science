def trim(string):
    while string[0] == " ":
        string = string[1:]

    while string[-1] == " ":
        string = string[:-1]

    return string


def index_of(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i

    return False

def split_by_first(string, char):
    """
        Принимает строку и символ, возвращает:
         - [char, part1, part2] если символ есть в строке
         - False - если символа в строке нет
        Внимание: функция стрипит пробелы у part1 part2
        Exmaple:
         - split('2 + 3', '+') = ['+', '2', '3']
         - split('2 + 3', '-') = False
    """
    index = index_of(string, char)

    if index != False:
        return [
            char,
            trim(string[:index]),
            trim(string[index+1:])
        ]
    else:
        return string

def replace(string, char, new_char):
    while index_of(string, char) != False:
        index = index_of(string, char)
        string = (string[:index] + new_char + string[index+1:])
    return string

def kebabToSnake(string):
    # kebabToSnake - превращает строки вида kabeab-to-snake в kebab_to_snake
    string = replace(string, "-", "_")
    return string

def kebabToCamel(string):
    # kebabToCamel - превращает строки вида kabeab-to-snake в kebabToCamel
    while index_of(string, "-") != False:
        index = index_of(string, "-")
        string = (string[:index] + string[index+1].upper() + string[index+2:])
    return string

def parentes(string):
    index = 0
    index_of_open_parentes = None

    open_parentes = count(string, "(")
    closing_parentes = count(string, ")")

    if open_parentes != closing_parentes:
        raise ValueError('Invalid math expression: ' + string)

    while index < len(string):
        if string[index] == "(":
            index_of_open_parentes = index
        elif string[index] == ")":
            return index_of_open_parentes, string[index_of_open_parentes+1:index]
        index += 1
    return None


def count(string, char):
    count_of = 0
    for i in string:
        if i == char:
            count_of += 1
    return count_of














  
