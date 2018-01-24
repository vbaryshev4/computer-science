class TestCase:
    def __init__(self, message):
        self.message = message
        return 

    def _check_has_attr(self):
        if not hasattr(self, 'expected'):
            raise Exception('Check called before .exptect()')

    def _result_struct(self, given, status, condition):
        return {
            'expected': self.expected,
            'given': given,
            'status': status,
            'message': self.message,
            'condition': condition
        }

    def expect(self, expected):
        self.expected = expected
        return self

    def to_be(self, given):
        self._check_has_attr()
        status = self.expected == given
        return self._result_struct(given, status, 'equality')

    def not_to_be(self, given):
        self._check_has_attr()
        status = self.expected != given
        return self._result_struct(given, status, 'non_quality')

    def to_greater(self, given):
        self._check_has_attr()
        status = self.expected > given
        return self._result_struct(given, status, 'greater')

    

