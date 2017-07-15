# Это файл пакета modules.tester и сюда мы импортируем все что должно лежать внутри modules.tester

import sys

from modules.tester.cases import *
from modules.tester.suite import Suite, test, Expectation

def expect(expected, indent = 2):
    return Expectation(expected, indent)

class TestNames():
    def __init__(self, scopes = {'*': []}):
        self.scopes = []
        for scope in scopes:
            setattr(self, scope, scopes[scope])
            if scope != '*':
                self.scopes.append(scope)
            

    def all(self):
        return getattr(self, '*') if hasattr(self, '*') else []

def get_test_names(lst):
    lst = lst[1:]

    if not len(lst):
        return TestNames({'*': ['*']})

    scopes = {
        '*': []
    }

    for item in lst:
        items = item.split('.')

        if len(items) == 2 and items[0] != '*':
            scopes[items[0]] = [items[1]] if not scopes.get(items[0]) else scopes[items[0]] + [items[1]]
            scopes['*'].append(items[1]) 
        else:
            scopes['*'].append(items[0])

    

    return TestNames(scopes)