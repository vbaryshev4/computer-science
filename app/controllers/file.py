from templates.pages.file_page import *

def file_controller(file_path):
    with open("app/pkgs/"+file_path, 'r') as content_file:
        content = content_file.read()
        file_path = file_path.split("/")[-1]

    res = file_page({
        'title': file_path,
        'body': content,
        'footer': 'Back',
        'styles':['/static/new.css']
        })

    return res


