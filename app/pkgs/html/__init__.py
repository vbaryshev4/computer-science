from html.pkgs.tag import Tag, Img, Heading, List
from html.pkgs.templates import render_test

def render_template():
    return render_test({
        'name': 'Shuffle test',
        'method': 'shuffle',
        'cases': [
            {
                'arguments': [1, 2, 3, 4, 5, 6, 7],
                'condition': {
                    'id': 'non_equality',
                    'value': [1, 2, 3, 4, 5, 6, 7]
                },
                'status': True,
                'message': 'Shuffles a list with ints'
            },
            {
                'arguments': ['a','b','c','d'],
                'condition': {
                    'id': 'non_equality',
                    'value': ['a','b','c','d']
                },
                'status': True,
                'message': 'Shuffles a list with str'
            },
                            {
                'arguments': [1, 2, 3, 'a', 'b', 'c'],
                'condition': {
                    'id': 'non_equality',
                    'value': [1, 2, 3, 'a', 'b', 'c']
                },
                'status': True,
                'message': 'Shuffles a list with mixed'
            },
        ],
        'status': True,
    })