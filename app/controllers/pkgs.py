from templates.pages.pkgs_page import *
from pkgs.fs import fs_read

def pkgs_controller():
    # Формирует объект данных
    tree = fs_read('./app/pkgs')
    # print('YO: 2.1', tree, '\n')

    # Формируем HTML-ответ
    html = pkgs_page(tree)
    # print('YO: 2.2', html, '\n')

    return html

