from pkgs.html import Tag

html = Tag('html')
body = Tag('body')
head = Tag('head')
title = Tag('title')
style = Tag('style')

def head_template(title_string, styles = []):
    styles_list = []
    for style_addr in styles:
        styles_list.append(
            style.render('', href=style_addr)
        )

    return head.render([
        title.render(title_string),
        style.render('', href="/static/main.css"),
        *styles_list
    ])


# {
    # 'title': 'Index', 
    # 'body': 
        # '<div class="container">
        # <h3>Index</h3>
        # <div class="content">Hello</div>
        # </div>', 
    # 'styles': ['/static/new.css']
# }

def html_page_template(data={}):
    res = html.render([
        head_template(
            data.get('title'), 
            data.get('styles')),
            body.render(data.get('body'))
        ])
    return res