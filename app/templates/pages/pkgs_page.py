from pkgs.html import Tag
from templates import body_template
from templates import html_page_template
from utils import generate_list




# def generate_list(*args):
#     '''

#     # Перенести логику из from utils import generate_list
#     # Для работы generate_list()
    
#     '''
#     return 'html'




def pkgs_page(data = {}):
    data = data.copy()

    # Step 1
    pkgs_content = generate_list('pkgs', data)
    # print('YO: 3.1', pkgs_content, '\n')


    # Step 2
    page_body = body_template({
        'heading': 'pkgs tree',
        'content': pkgs_content,
    })
    # print('YO: 3.2', page_body, '\n')

    # Step 3
    final_html = html_page_template({
        'title': 'pkgs tree',
        'body': page_body
    })
    # print('YO: 3.3', final_html, '\n')

    return final_html
