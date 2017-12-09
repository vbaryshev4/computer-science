from pkgs.html import Tag
from templates import body_template, html_page_template

div = Tag('div')
a = Tag('a')

def index_page(data = {}):
    data = data.copy()

    # Step 1
    index_page_content = [
        div.render([
            'Author: ',
            a.render('vbaryshev', href='https://github.com/vbaryshev4')
        ])
    ]

    # Step 2
    page_body = body_template({
        'heading': data.get('title'),
        'content': index_page_content
    })

    # Step 3
    final_html = html_page_template({
        'title': data.get('title'),
        'body': page_body
    })
    return final_html