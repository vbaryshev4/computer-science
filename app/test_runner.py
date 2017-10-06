from app.pkgs.lists.test import ListTests
from app.pkgs.strings.test import StringTest
from app.pkgs.func.test import FuncTest
from app.pkgs.calc.test import CalcTest

list_test = ListTests()
list_test.run()

strings_test = StringTest()
strings_test.run()

func_test = FuncTest()
func_test.run()

calc_test = CalcTest()
calc_test.run()
