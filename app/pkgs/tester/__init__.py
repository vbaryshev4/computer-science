# Это файл пакета pkgs.tester и сюда мы импортируем все что должно лежать внутри pkgs.tester

from pkgs.tester.cases import *
from pkgs.tester.suite import Suite
from pkgs.tester.TestCase import TestCase

def test(test_name, test_method):
    def decorator(fn):
        def decorated(self):
            if not hasattr(self, 'tests'):
                self.tests = []

            self.tests.append({
                'name': test_name,
                'method': test_method,
                'fn': fn,
            })
        return decorated
    return decorator