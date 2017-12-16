from templates.pages.pkgs_page import *
from pkgs.fs import fs_read

def pkgs_controller():
    # Формирует объект данных
    tree = fs_read('./app/pkgs')

    # Формируем HTML-ответ
    html = pkgs_page(tree)

    return html

