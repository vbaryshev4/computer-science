from pkgs.html import Tag

div = Tag('div')
hr = Tag('hr')
a = Tag('a')
pre = Tag('pre')
code = Tag('code')

from templates import body_template
from templates import html_page_template

def file_page(data):
    data = data.copy()

    content = [
        pre.render(code.render(data.get('file_content'), class_name='content'), class_name='python'),
        hr.render(''),
        a.render('Back', href='/')
    ]

    data['body'] = body_template({
        'heading': data.get('title'),
        'content': content,
    })
    
    res = html_page_template(data)

    return res
