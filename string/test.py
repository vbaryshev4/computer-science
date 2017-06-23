import sys
sys.path.insert(0, '/Users/vbaryshev/Documents/Python files/Trdat/computer-science')

from tester.tester import *
from string.string import *

equality_case(trim('  a'), 'a', 'Should trim spaces from start of string')
equality_case(trim('a   '), 'a', 'Should trim spaces from end of string')
equality_case(kebabToSnake("kabeab-to-snake"), 'kabeab_to_snake', 'Should change all - to _')
equality_case(kebabToCamel("kabeab-to-camel"), 'kabeabToCamel', 'Should return camelCase string')