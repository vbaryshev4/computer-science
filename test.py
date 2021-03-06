#!/usr/local/bin/python3.6

from pkgs.lists.test import ListTests
from pkgs.strings.test import StringTest
from pkgs.func.test import FuncTest
from pkgs.calc.test import CalcTest

list_test = ListTests()
list_test.run()

strings_test = StringTest()
strings_test.run()

func_test = FuncTest()
func_test.run()

calc_test = CalcTest()
calc_test.run()
