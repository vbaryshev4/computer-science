import os
from flask import Flask, request

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
"""

def get_body(data):
    ul = '<ul>{items}</ul>'
    li = '<li>{str}</li>\n\t\t'
    items = ''
    for i in data:
        items += li.format(str=i)
    return ul.format(items=items)


@app.route('/')
def index():
    names_data = [
    'Joe',
    'Vasily']
    return template.format(
        title='My awesome site',
        body=get_body(names_data)
    )

@app.route('/pkgs')
def pkgs():
    # Processing of HTTP request comes here
    return template.format(
        title='pkgs stats',
        body='<h1>pkgs statistics</h1>'
    )


@app.route('/tree')
def tree():
    pkgs = []
    counts = []
    for root, dirs, files in os.walk('/Users/vbaryshev/Documents/Python_files/Trdat/computer-science/pkgs/'):
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        if '__init__.py' in files:
            files.remove('__init__.py')
        if '.DS_Store' in files:
            files.remove('.DS_Store')
    
        root_level = 0
        while root_level != 1:
            root_level += 1

        pkgs.append(dirs)
        counts.append(len(files))

    pkgs = pkgs[root_level-1]
    counts = counts[root_level:]

    result = []
    for i in range(len(pkgs)):
        result.append(pkgs[i]+ " " +str(counts[i]))

    return template.format(title='Server tree', body=get_body(result))

# Preferences
app.run(port=8080, debug=True)