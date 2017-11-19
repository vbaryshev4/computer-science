from pkgs.html import Tag

li = Tag('li')
p = Tag('p')
div = Tag('div')
code = Tag('code')
h4 = Tag('h4')
h5 = Tag('h5')
ol = Tag('ol') 


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
            code.render(str(case['arguments']))
        ]),
        div.render([
            p.render('Conditions',
                class_name='condition-title'
            ),
            p.render([
                'ID:',
                code.render(case['condition']['id'])
            ]),
            p.render([
                'Value',
                code.render(str(case['condition']['value']))
            ]),
        p.render(case['message'])
        ], class_name='conditions')
    ]

    return li.render(body, 
        class_name=class_name
        )
