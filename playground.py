import pkgs.tools.main


### Обход файловой структуры

# Необходимо написать функцию `read_fs`, 
# которая принимает строку - это путь к дирректории. 
# Она обходит дирректорию рекурсивно 
# и выводит структуру следующего вида: 

'''
{'files': ['__init__.py', 'a.py', 'b.py'], 'dirs': {'dir1' : {'files': ['__init__.py', 'b.py'],'dirs': {'empty_dir': {}}},'dir2': {'files': ['one.py', 'two.py']}}}
'''

# Такая структура данных соответствует следующей файловой структуре: 

'''
>>> fs_read('./root')

# треугльником отмечены папки
# звездочкой файлы

> root
...> dir1
......> empty_dir #пустая папка
......* __init__.py
......* b.py
...> dir2
......* one.py
......* two.py
...* __init__.py
...* a.py
...* b.py
'''

### Некоторые условия и подсказки
'''
 - fs_read рекурсивна
 - Если fs_read передать путь до пустой дирректории - 
   она вернет пустой список (это зерно рекурсии)
 - Внутри тела функции должно быть определения - это файл или дирректория

Тебе точно пригодятся
 - [os.listdir](https://docs.python.org/3/library/os.html#os.listdir)
 - [os.path.join](https://docs.python.org/3/library/os.path.html#os.path.join)
 - [os.path.isdir](https://docs.python.org/3/library/os.path.html#os.path.isdir)
 - [os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile)
'''

import os

def clear_out(lst): #Clears out of system and cache files and dirs
    result = []
    for i in lst:
        if i.startswith('.') or i.startswith('__pycache__'):
            continue
        else:
            result.append(i)
    return result


def path_and_verify(path): #Makes paths with a name of files and dirs
    
    result = {"files":[], "dirs":{}} 
    files = []
    dirs = {}

    for i in clear_out(os.listdir(path)):
        new_path = os.path.join(path,i)
        if os.path.isdir(new_path):
            dirs.update({i:path_and_verify(new_path)})
            # return path_and_verify(new_path)

        elif os.path.isfile(new_path):
            files.append(i)
    
    result.update({"files":files}) or result.update({"dirs":dirs})

    if files is [] and dirs is {}:
        return result

    return result

print(path_and_verify("."))

'''
{'files': 
    ['computer-science.sublime-project', 
    'computer-science.sublime-workspace', 
    'playground.py', 
    'README.md', 
    'requirements.txt', 
    'test.py'], 
'dirs': 
    {'app': 
        {'files': 
            ['__init__.py'], 
        'dirs': {}},

    'homework': 
        {'files': 
            [], 
        'dirs': {
            '01':{
                'files': 
                    ['homework.md', 
                    'README.md'], 
                'dirs': 
                    {}}, 
            '02': {
                'files': 
                    ['README.md'], 
                'dirs': 
                    {}}, 
            '03': {
                'files': 
                    ['classes_explanation_example.py', 
                    'README.md'], 
                'dirs': {}}, 
            '04': {
                'files': 
                    ['README.md'], 
                'dirs': {}}, 
            '05': {
                'files': 
                    ['README.md'], 
                'dirs': {}}, 
            '06': {
                'files':
                    ['hw_06_closures_reverse.py', 
                    'hw_06_funcs.py', 
                    'hw_06_Scopes.py', 
                    'README.md'], 
                'dirs': {}}, 
            '07': {
                'files': 
                    ['hw_07_funcs.py', 
                    'README.md'], 
                'dirs': {}}, 
            '08': {
                'files': 
                    ['README.md'],
                    'dirs': {}}, 
            '09': {
                'files': 
                    'README.md'],
                dirs': {}}, 
            '10': {
                'files': [], 
                'dirs': {}}}}, 
    'pkgs': {
        'files': 
            ['__init__.py'], 
        'dirs': {
            'calc': 
                {'files': 
                ['__init__.py', 
                'calc.py', 
                'test.py'], 
            'dirs': {}}, 
            'func': {
                'files': 
                    ['__init__.py', 
                    'main.py', 
                    'test.py'], 
                    'dirs': {}}, 
                'lists': {
                    'files': 
                        ['__init__.py', 
                        'flatten_reverse_engineering.py', 
                        'main.py', 
                        'test.py'], 
                    'dirs': {}}, 
                'strings': {
                    'files': 
                        ['__init__.py', 
                        'main.py', 
                        'test.py'], 
                    'dirs': {}}, 
                'tester': {
                    'files': 
                        ['__init__.py', 
                        'cases.py', 
                        'suite.py'], 
                    'dirs': {}}, 
                'tools': {
                    'files': 
                        ['__init__.py',
                        'main.py'], 
                    'dirs': {}}}}}}
'''