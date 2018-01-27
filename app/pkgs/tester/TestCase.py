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
}

class TestCase:
    def __init__(self, message):
        self.message = message
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

    def _exec_test(self, type_of_test, expected):
        self._check_has_attr()
        status = checks[type_of_test](self.given, expected)
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

    def to_raise(self, expected_type_of_error = Exception):
        return self._exec_test('raise', expected_type_of_error)

    # def to_be_type(self, expected):
    #     self._check_has_attr()
    #     status = type(self.given) == expected:
    #     return self._exec_test(expected, status, 'type')

    # def to_be_instance(self, expected):
    #     self._check_has_attr()
    #     status = instance(self.given, expected)
    #     return self._exec_test(expected, status, 'instance')

    # def to_has_attr(self, expected):
    #     self._check_has_attr()
    #     status = hasattr(self.given, expected)
    #     return self._exec_test(expected, status, 'has_attr')

    # def to_has_method(self, expected):
    #     self._check_has_attr()
    #     status = hasattr(self.given, expected) and callable(getattr(self.given, expected))
    #     return self._exec_test(expected, status, 'has_method')

