from pkgs.calc import * 
from pkgs.tester import *

class Tests(Suite):
    module = "pkgs.calc"
    name = 'Calc Module Tests'
    description = 'Tests for module calc'

    @test('Calc', 'calc_test')
    def calc_test():
        yield TestCase(
            'Should return a result of calculation: string case'
        ).expect(
            calc("qwe")
        ).to_be('qwe')

        yield TestCase(
            'Should return a result of calculation: integers case'
        ).expect(
            calc("1+2-3")
        ).to_be(0)    
