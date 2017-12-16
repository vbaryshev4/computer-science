from pkgs.html import Tag
from templates import body_template
from templates import html_page_template
from utils import generate_list

# {'files': ['__init__.py'], 
# 'dirs': {'strings': {'files': ['__init__.py', 'test.py', 'main.py'], 'dirs': {}},
# 'tools': {'files': ['__init__.py', 'main.py'], 'dirs': {}}, 
# 'types': {'files': ['Queue.py', 'number.py', '__init__.py', 'Point.py', 'liked_list.py', 'Math.py'], 'dirs': {}}, 
# 'lists': {'files': ['__init__.py', 'test.py', 'flatten_reverse_engineering.py', 'main.py'], 'dirs': {}}, 
# 'html': {'files': ['__init__.py', 'tag.py'], 'dirs': {}}, 
# 'calc': {'files': ['__init__.py', 'test.py', 'calc.py'], 'dirs': {}}, 
# 'api': {'files': ['__init__.py', 'main.py'], 'dirs': {}}, 
# 'tester': {'files': ['suite.py', '__init__.py', 'cases.py'], 'dirs': {}}, 
# 'fs': {'files': ['__init__.py', 'main.py'], 'dirs': {}}, 
# 'func': {'files': ['__init__.py', 'test.py', 'main.py'], 'dirs': {}}}}


div = Tag('div')
hr = Tag('hr')
a = Tag('a')
pre = Tag('pre')
code = Tag('code')

def generate_list(*args):
    '''

    # Перенести логику из from utils import generate_list
    # Для работы generate_list()
    
    '''
    return 'html'


def pkgs_page(data = {}):
    data = data.copy()

    # Step 1
    pkgs_content = generate_list('pkgs', data)

    # Step 2
    page_body = body_template({
        'heading': 'pkgs tree',
        'content': pkgs_content,
    })

    # Step 3
    final_html = html_page_template({
        'title': 'pkgs tree',
        'body': page_body
    })

    return final_html
