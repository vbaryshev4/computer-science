#!/usr/local/bin/python3.6

import sys

from modules.lists.test import ListTests
from modules.string.test import StringTests

from modules.tester import get_test_names

test_names = get_test_names(sys.argv)

list_test = ListTests('lists')
string_test = StringTests('string')

list_test.run(test_names)
string_test.run(test_names)

