from pkgs.html import *
from templates import body_template
from templates import html_page_template

heading = Heading(3)

def render_files(files, path = []):
    res = []

    for file_name in files:
        ext = '/'.join(path + [file_name])
        file_path = '/file/{0}'.format(ext)
        file_link = a(file_name, href=file_path)
        li_content = [file_link]

        if file_name == 'test.py':
            test_link = '/test/' + '/'.join(path) + '/'
            li_content += ['...', a('(▶ run test)', href=test_link)]

        res.append(li(li_content))

    return res


def render_dirs(dirs, path):
    dirs_items = []

    for dir_name in dirs:
        dirs_items.append(render_tree(
            dir_name,
            dirs[dir_name],
            path + [dir_name]
        ))

    return dirs_items


def render_tree(root_name, tree, path = []):
    files_count = len(tree['files'])

    files_items = render_files(tree['files'], path)
    dirs_items = render_dirs(tree['dirs'], path)

    return div([
        heading([root_name, '(', str(files_count), ')']),
        ul([
            *dirs_items,
            *files_items
        ])
    ], class_name='tree')


def pkgs_page(tree = {}):
    tree = tree.copy()

    # Step 1
    pkgs_content = render_tree('pkgs', tree)
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
