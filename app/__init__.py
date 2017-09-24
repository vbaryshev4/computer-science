import os
from flask import Flask, request
from pkgs.fs import *
from utils import generate_list

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="/static/main.css">
        <title>{title}</title>
    </head>
    <body>
        <main>
            {body}
        </main>
    </body>
</  html>
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

    body = ''

    tree = fs_read('./app/pkgs')
    body = generate_list('pkgs', tree)

    # body = fs_read('./pkgs')['dirs'].keys()

    return template.format(
        title='pkgs stats',
        body='<h1>pkgs statistics</h1>' + body
    )

# http://flask.pocoo.org/snippets/76/
@app.route('/file/<path:file_path>')
def file(file_path):
    return file_path

# Preferences
app.run(port=8080, debug=True)