from templates.pages import index_page

# http://127.0.0.1:8080/file/calc/calc.py
def file_controller(file_path):
    with open("app/pkgs/"+file_path, 'r') as content_file:
        content = content_file.read()

    res = index_page({
        'title': 'Index',
        'body': content,
        'styles': [
            '/static/new.css']
        })

    return res


