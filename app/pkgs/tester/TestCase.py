def raise_check(a, b):
    try:
        a()
        return False
    except b:
        return True

checks = {
    'equality': lambda a, b: a == b,
    'non_quality': lambda a, b: a != b,
    'greater': lambda a, b: a > b,
    'smaller': lambda a, b: a < b,
    'raise': raise_check,
    'has_attr': lambda a, b: hasattr(a, b),
    'type': lambda a, b: type(a) == b,
    'instance': lambda a, b: instance(a, b),
    'has_attr': lambda a, b: hasattr(a, b),
    'has_method': lambda a, b: hasattr(a, b) and callable(getattr(a, b))
    }

class TestCase:
    def __init__(self, message):
        self.message = message
        self.res_inversion = None
        return

    def _check_has_attr(self):
        if not hasattr(self, 'given'):
            raise Exception('Check called before .expect()')

    def _result_struct(self, expected, status, condition):
        return {
            'given': self.given,
            'expected': expected,
            'status': status,
            'message': self.message,
            'condition': condition
        }

    def _not(self):
        self.res_inversion = True
        return self

    def _exec_test(self, type_of_test, expected):
        self._check_has_attr()
        status = checks[type_of_test](self.given, expected)
        if self.res_inversion == True:
            status = not status
        return self._result_struct(expected, status, type_of_test)

    def expect(self, given):
        self.given = given
        return self

    def to_be(self, expected):
        return self._exec_test('equality', expected)

    def not_to_be(self, expected):
        return self._exec_test('non_equality', expected)

    def to_greater_then(self, expected):
        return self._exec_test('greater', expected)

    def to_smaller_then(self, expected):
        return self._exec_test('smaller', expected)

    def to_raise(self, expected_type_of_error=Exception):
        return self._exec_test('raise', expected_type_of_error)

    def to_be_type(self, expected):
        return self._exec_test('type', expected)

    def to_be_instance(self, expected):
        return self._exec_test('instance', expected)

    def to_has_attr(self, expected):
        return self._exec_test('has_attr', expected)

    def to_has_method(self, expected):
        return self._exec_test('has_method', expected)