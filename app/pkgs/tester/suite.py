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
        has_test_fn = False

        for attr in attrs:
            if attr.endswith("_test"):
                method = getattr(self, attr)
                name = attr.replace('_test', '')

                if testfn == "main" or testfn == name:
                    print("Function: {0}".format(name))
                    method()
                    print('\n')
                    has_test_fn = True

        if not has_test_fn:
            print("----")
            print("No function: {0} in {1} \n".format(testfn, self.module))

        return 'yay!!'