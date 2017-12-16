from templates.pages.file_page import *

def file_controller(file_path):
    with open('app/pkgs/' + file_path, 'r') as content_file:
        content = content_file.read()
        file_name = file_path.split("/")[-1]

    # Формирует объект данных
    file_data = {
        'file_path': file_path,
        'file_name': file_name,
        'file_content': content,
    }

    # Формируем HTML-ответ
    html = file_page(file_data)

    return html
