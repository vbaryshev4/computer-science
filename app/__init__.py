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

'''
    <h1>Header</h1>
    <hr>
    <pre>code</pre>
    <hr>
    <a href="">Back</a>
'''


@app.route('/')
def index():
    return template.format(
        title='My awesome site',
        body="<h1>pkgs UI kit</h1>"
    )

@app.route('/pkgs/')
def pkgs():
    tree = fs_read('./app/pkgs')
    body = generate_list('pkgs', tree)

    return template.format(
        title='pkgs stats',
        body='<h1>pkgs statistics</h1>' + body
    )

def render_code(path, content):

    a = '''
        <h1>{header}</h1>
        <hr>
        <pre><code class="python">{code}</code></pre>
        <hr>
        <a href="/pkgs/">Back</a>
    '''
    file_name = path.split("/")[-1]
    result = a.format(header=file_name, code=content)
    return result

# http://flask.pocoo.org/snippets/76/
@app.route('/file/<path:file_path>')
def file(file_path):
    with open("app/pkgs/"+file_path, 'r') as content_file:
        content = content_file.read()
    return template.format(
        title='{0} - code content'.format(file_path),
        body=render_code(file_path, content)
    )


# Preferences
app.run(port=8080, debug=True)