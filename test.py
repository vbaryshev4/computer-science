#!/usr/local/bin/python3.6

from pkgs.lists.test import ListTests
from pkgs.strings.test import StringTest

list_test = ListTests()
list_test.run()

strings_test = StringTest()
strings_test.run()

