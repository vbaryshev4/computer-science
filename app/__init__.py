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

# path = "/Users/vbaryshev/Documents/Python_files/Trdat/computer-science/pkgs/"

@app.route('/tree')
def tree():
    path = "/Users/vbaryshev/Documents/Python_files/Trdat/computer-science/pkgs/"
    tree = []
    i = 0
    for (path, dirs, files) in os.walk(path):
        tree.append(dirs[1::]) #Написать функцию, которая чистит список от заданных аргументов
        # print(dirs)
        i += 1
        if i >= 1:
            break

    return template.format(
    title='Server tree', body=get_body(tree[0]))


# Preferences
app.run(port=8080, debug=True)