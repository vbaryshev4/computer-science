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
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css">

        <title>{title}</title>
    </head>
    <body>
        <main>
            {body}
        </main>
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
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

@app.route('/pkgs/')
def pkgs():
    tree = fs_read('../app/pkgs')
    body = generate_list('pkgs', tree)

    return template.format(
        title='pkgs stats',
        body='<h1>pkgs statistics</h1>' + body
    )

# http://flask.pocoo.org/snippets/76/
@app.route('/<path:file_path>')
def file(file_path):
    with open(file_path, 'r') as content_file:
        content = content_file.read()
    return template.format(
        title='{0} - code content'.format(file_path),
        body=content
    )


# Preferences
app.run(port=8080, debug=True)