from pkgs.html import Tag

html = Tag('html')
body = Tag('body')
head = Tag('head')
title = Tag('title')
link = Tag('link', rel='stylesheet')
script = Tag('script', type='text/javascript')

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
        link.render('', href='//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css'),
        *styles_list
    ])

def scripts(scripts = []):
    scripts_content = []
    for src in scripts or []    :
        scripts_content.append(script.render('', src=src))

    scripts_content += [
        script.render('', src='//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js'),
        script.render('hljs.initHighlightingOnLoad();'),
    ]

    return ''.join(scripts_content)

def html_page_template(data={}):
    res = html.render([
        head_template(
            data.get('title'), 
            data.get('styles')
        ),
        body.render([
            data.get('body'),
            scripts(data.get('scripts'))
        ])
    ])

    return res
