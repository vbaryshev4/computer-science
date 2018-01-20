from pkgs.html import *
from templates import body_template
from templates import html_page_template

def test_page(data = {}):
    data = data.copy()

    # Step 1
    test_page_content = []
    if data['error']:
        test_page_content.append(('ERROR: "{}"').format(
            data['message'])
        )
    else:
        test_page_content.append('OK')

    # Step 2
    page_body = body_template({
        'heading': data.get('pkg_name'),
        'content': test_page_content,
    })

    # Step 3
    final_html = html_page_template({
        'title': 'Test result for: ' + data.get('pkg_name'),
        'body': page_body
    })

    return final_html
