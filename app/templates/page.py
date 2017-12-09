from pkgs.html import Tag

html = Tag('html')
body = Tag('body')
head = Tag('head')
title = Tag('title')
link = Tag('link', rel='stylesheet')

def head_template(title_string, styles = []):
    styles_list = []
    for style_addr in styles or []:
        styles_list.append(
            link.render('', href=style_addr)
        )

    return head.render([
        title.render(title_string),
        link.render('', href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'),
        link.render('', href='/static/main.css'),
        *styles_list
    ])


def html_page_template(data={}):
    res = html.render([
        head_template(
            data.get('title'), 
            data.get('styles')),
            body.render(data.get('body'))
            
        ])
    return res



