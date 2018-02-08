from pkgs.func import *
from pkgs.tester import *

class Tests(Suite):
    module = "pkgs.func"
    name = 'Func Module Tests'
    description = 'Tests for module func'

    @test('Times test', 'times_test')
    def times_test():
        yield TestCase(
            'Print a sum of args one time'
        ).expect(
            times(print_sum, 1, 10, 3)
        ).to_be([13])

        yield TestCase(
            'Print a sum of args four time'
        ).expect(
            times(print_sum, 4, 10, 3)
        ).to_be([13, 13, 13, 13])

        yield TestCase(
            'Print a sum of args zero time'
        ).expect(
            times(print_sum, 0, 10, 3)
        ).to_be([])     
