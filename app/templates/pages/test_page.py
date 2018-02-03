from pkgs.html import *
from templates import body_template
from templates import html_page_template

def render_all_tests(tests):
    body = [
        p(['Name:', tests['name']]),
        p(['Description: ', tests['description']]),
    ]

    for test in tests['tests']:
        body.append(render_test(test))

    return body

def render_test(test):
    body = [ 
        h4.render(test['name']),
        p.render([
            'Method: ',
            code.render(test['method'])
        ]),
        p.render([
            'Status: ',
            code.render(test['status'])
        ], class_name='status'),
        h5.render('Cases'),
        ol.render(list(map(render_case, test['cases'])))
    ]

    return li.render(body, class_name='test')

def render_case(case):    
    if case['status']:
        class_name = "testcase success"
        status_string = 'Status: OK'
    else:
        class_name = "testcase fail"
        status_string = 'Status: Fail'

    body = [
        p.render(status_string, class_name='status'),
        p.render([
            'Arguments: ',
            code.render(str(case['given']))
        ]),
        p.render([
            'Expected: ',
            code.render(str(case['expected']))
        ]),
        div.render([
            p.render(['Condition: ', code.render(str(case['condition']))],
                class_name='condition-title'
            ),
        p.render(case['message'])
        ], class_name='conditions')
    ]

    return li.render(body, 
        class_name=class_name
        )


def test_page(data = {}):
    data = data.copy()

    # Step 1
    test_page_content = []
    if data['error']:
        test_page_content.append(('ERROR: "{}"').format(
            data['message'])
        )
    else:
        test_page_content = render_all_tests(data['results'])
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
