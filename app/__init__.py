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

data = [
    'Joe',
    'Vasily'
]

def get_body(data):
    ul = '<ul>{items}</ul>'
    li = '<li>{str}</li>\n'
    items = ''
    for i in data:
        items += li.format(str=i)
    return ul.format(items=items)


@app.route('/')
def index():
    return template.format(
        title='My awesome site',
        body=get_body(data)
    )

@app.route('/pkgs')
def pkgs():
    # Processing of HTTP request comes here
    return template.format(
        title='pkgs stats',
        body='<h1>pkgs statistics</h1>'
    )

app.run(port=8080, debug=True)