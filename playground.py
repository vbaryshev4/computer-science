# import pkgs.tools.main
import os

def clear_out(lst): #Clears out of system and cache files and dirs
    result = []
    for i in lst:
        if i.startswith('.') or i.startswith('__pycache__'):
            continue
        else:
            result.append(i)
    return result


def path_and_verify(path): #Makes paths with a name of files and recoursive dirs
    
    result = {"files":[], "dirs":{}} 
    files = []
    dirs = {}

    for i in clear_out(os.listdir(path)):
        new_path = os.path.join(path,i)
        if os.path.isdir(new_path):
            dirs.update({i:path_and_verify(new_path)})

        elif os.path.isfile(new_path):
            files.append(i)
    
    result.update({"files":files}) or result.update({"dirs":dirs})

    return result

print(path_and_verify("."))

# STDOUT EXAMPLE
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