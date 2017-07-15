import types
from modules.tester.colors import red, green, bold, cyan

reservedMethods = [
    'run',
    'expect',
    'getTests',
]

def test(name):
    def decorating(fn):
        def decorated(*args):
            self = args[0]
            tests = list(args[1:])
            
            if name not in tests and tests != ['*']:
                return

            try:
                print('---------------- {} ::'.format(bold(self.name + '.' + name)))
                block = fn(self)
                if isinstance(block, types.GeneratorType):
                    while True:
                        try:
                            case = block.send(None)
                            if case.msg == '':
                                case.msg = '{0} : {1}'.format(name, case.body)
                            case.exec()
                            # print('---')
                        except StopIteration:
                            break
            except Exception as e:
                print('Exception:', e)
            print('\n')
        return decorated
    return decorating


def reporter(scope, name, cases, obj):
    print('---------------- {} ::'.format(bold(scope + '.' + name)))
    block = cases(obj)



class Suite():
    """
        Базовый класс для создания юнит-тестов
    """

    def __init__(self, name):
        self.name = name


    def getTests(self, test_names):
        if not test_names or len(test_names.scopes) == 0:
            return test_names.all()

        if self.name not in test_names.scopes:
            return []

        return getattr(test_names, self.name)

    def run(self, test_names = None):
        tests = self.getTests(test_names)
        test_blocks = []

        for attr in dir(self):
            method = getattr(self, attr)
            if attr not in reservedMethods and callable(method) \
                and not attr.startswith('__') and not attr.endswith('__'):
                    method(*tests)

    def expect(self, expected):
        return Expectation(expected, 2)

    # def case(self, fn):
    #     gen = fn(self)
    #     while True:
    #         t = gen.send(None)
    #         t.exec()

class Expectation():
    def __init__(self, body, indent = 0):
        self.body = body
        self.indent = indent
        self.msg = ''

    def stdout(self, msg):
        print(' ' * self.indent + msg)

    def toBe(self, value):
        def comprator(a, b):
            return a == b
        self.value = value
        self.comprator = comprator
        self.error = 'Expect: {0.body} to be equal: {0.value}'.format(self)
        return self

    def notToBe(self, value):
        def comprator(a, b):
            return a != b
        self.value = value
        self.comprator = comprator
        self.error = 'Expect: {0.body} not to be equal: {0.value}'.format(self)
        return self

    def toRaise(self, value = Exception):
        def comprator(a, b):
            try:
                a()
            except Exception as e:
                if isinstance(e, value):
                    return True
            return False
        self.value = value
        self.comprator = comprator
        self.error = 'Expect: to raise an Exception'
        return self

    def message(self, msg):
        self.msg = msg
        return self

    def toFalse(self, msg):
        def comprator(a, b):
            return a == False
        self.msg = msg
        self.value = False
        self.comprator = comprator
        self.error = 'Expect False value'
        return self

    def exec(self):
        result = self.comprator(self.body, self.value)
        message = green('✔') if result else red('✘ Failed: {.error}'.format(self))
        self.stdout(cyan(self.msg) + ' ' + message)