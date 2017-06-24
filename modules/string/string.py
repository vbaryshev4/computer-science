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


    