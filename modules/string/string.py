#!/usr/local/bin/python3.6

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
    return -1

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
    while index_of(string, char) != -1:
        index = index_of(string, char)
        string = (string[:index] + new_char + string[index+1:])
    return string

def kebabToSnake(string):
    # kebabToSnake - превращает строки вида kabeab-to-snake в kebab_to_snake
    string = replace(string, "-", "_")
    return string

def kebabToCamel(string):
    # kebabToCamel - превращает строки вида kabeab-to-snake в kebabToCamel
    while index_of(string, "-") != -1:
        index = index_of(string, "-")
        string = (string[:index] + string[index+1].upper() + string[index+2:])
    return string


def capitalize(string):
    """
        Принимает строку и заменяет первую букву каждого слова на заглавную.
        Слова отделяются друг от друга пробелами и переходом строки
        'this is my world' -> 'This Is My World'
        'hello' -> 'Hello'
        'one \ntwo' -> 'One \nTwo'
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


def parentesize(string):
    """
        Принимает строку, которая может содержать скобки. 
        Возвращает кортеж из двух элементов, где: 
        1-й элемент - это исходная строка, но первое корректное вхождение выражения
        внутри скобок заменено на символ $
        2-й элемент - это то, что находилось в этих скобках
        parentesize('1 + (3 + 8)') # возвращает ('1 + $', '3 + 8')
        parentesize('1 + 3') # возвращает ('1 + 3', None)
        parentesize('(b + c)') # возвращает ('$', 'b + c')
    """
    i = index_of(string, "(")
    if i == -1:
        return string, None
    else:
        new_string = string[:i] + "$", replace(string[i+1:], ")", "")
        return new_string


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
