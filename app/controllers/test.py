from templates.pages.test_page import *

def package_test_controller(pkg_name):

    try:
        pkgs = __import__('pkgs.' + pkg_name + '.test')
    except:
        data = {
            'error': True,
            'message': 'Package {} not found'.format(pkg_name)
        }
    else:
        pkg = getattr(pkgs, pkg_name)

        if not hasattr(pkg, 'test'):
            data = {
                'error': True,
                'message': 'There is no tests for "{}" package'.format(pkg_name)
            }
        else:
            test = getattr(pkg, 'test')
            cases = test.Tests()
            data = {
                'error': False,
                'results': cases.run()
            }

    data['pkg_name'] = pkg_name

    return test_page(data)

