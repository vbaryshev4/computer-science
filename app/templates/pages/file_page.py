from pkgs.html import *
from templates import body_template
from templates import html_page_template

def file_page(data = {}):
    data = data.copy()

    # Step 1
    file_page_content = [
        pre.render(code.render(data.get('file_content'), class_name='content'), class_name='python'),
        div.render('File path: ' + data.get('file_path'), class_name='path'),
        hr.render(''),
        a.render('Back', href='/pkgs/')
    ]

    # Step 2
    page_body = body_template({
        'heading': data.get('file_name'),
        'content': file_page_content,
    })

    # Step 3
    final_html = html_page_template({
        'title': 'Content of file: ' + data.get('file_path'),
        'body': page_body
    })

    return final_html
