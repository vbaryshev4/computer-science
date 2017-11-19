from pkgs.html.tag import Tag, Img
from pkgs.html.templates import render_case

def render_template():
    return render_case({
        'arguments': [1, 2, 3, 4, 5, 6, 7],
        'condition': {
            'id': 'non_equality',
            'value': [1, 2, 3, 4, 5, 6, 7]
        },
        'status': True,
        'message': 'Shuffles a list with ints'
    })