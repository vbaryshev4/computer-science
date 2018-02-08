import sys

testfn = "main"

try:
    testfn = sys.argv[1]
except IndexError:
    pass

class Suite():

    """
        Базовый класс для создания юнит-тестов
    """
    def run(self):
        attrs = dir(self)

        for attr in attrs:
            attr_value = getattr(self, attr)
            if attr.endswith("_test") and callable(attr_value):
                attr_value()

        tests = []

        for test in self.tests:
            test_result = {
                'name': test['name'],
                'method': test['method'],
                'cases': [],
                'status': True
            }
            gen = test['fn']()
            while True:
                try:
                    case_res = gen.send(None)
                    test_result['cases'].append(case_res)
                    if not case_res['status']:
                        test_result['status'] = False
                except StopIteration:
                    break
                except Exception as err:
                    print(err)
            tests.append(test_result)
        
        return {
            'name': self.name,
            'description': self.description,
            'module': self.module,
            'tests': tests
        }




