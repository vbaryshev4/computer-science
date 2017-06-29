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

def capitalize(string):
    """
        Принимает строку и заменяет первую букву каждого слова на заглавную.
        Слова отделяются друг от друга пробелами и переходом строки
        'this is my world' -> 'This Is My World'
        'hello' -> 'Hello'
        'one
        two' -> 
        'One
        Two'
    """
    
    pass

def paretntesize(string):
    """
        Принимает строку, которая может содержать скобки. 
        Возвращает кортеж из двух элементов, где: 
        1-й элемент - это исходная строка, но первое корректное вхождение выражения
        внутри скобок заменено на символ $
        2-й элемент - это то, что находилось в этих скобках
        paretntesize('1 + (3 + 8)') # возвращает ('1 + $', '3 + 8')
        paretntesize('1 + 3') # возвращает ('1 + 3', None)
        paretntesize('(b + c)') # возвращает ('$', 'b + c')
    """
    pass
