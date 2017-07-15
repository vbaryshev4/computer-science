from modules.string import *
from modules.tester import * 

class StringTests(Suite):
    @test('trim')
    def _trim(self):
        yield expect(trim('')).toBe('').message('Should work with empty string')
        yield expect(trim('  a')).toBe('a').message('Should trim spaces from start of string')
        yield expect(trim('a   ')).toBe('a').message('Should trim spaces from end of string')
        yield expect(trim('   a   ')).toBe('a').message('Should trim spaces from start & end of string')

    @test('kebab')
    def _kebab(self):
        yield expect(kebab_to_snake("kabeab-to-snake")).toBe('kabeab_to_snake').message('Should change all - to _')
        yield expect(kebab_to_camel("kabeab-to-camel")).toBe('kabeabToCamel').message('Should return camelCase string')

    @test('parentes')
    def _parentes(self):
        yield expect(parentes("1+(2+3)")).toBe(
            (2, "2+3")
        ).message("Should work correctly")

        yield expect(parentes("1+3")).toBe(
            (-1, None)
        ).message("Should return None if not found")

        yield expect(
            lambda:parentes('(')
        ).toRaise(
            ValueError
        ).message('Should raise ValueError on invalid expression')

    @test('count')
    def _count(self):
        yield expect(count("(((", "(")).toBe(3)
        yield expect(count("+-+++--", "+")).toBe(4)
        yield expect(count("aAaAAA", "a")).toBe(2)
        yield expect(count("?###!%", "?")).toBe(1)
        yield expect(count("?###!%", "#")).toBe(3)

    @test('capitalize')
    def _capitalize(self):
        yield expect(capitalize('this is my world')).toBe('This Is My World').message("Should work correctly")
        yield expect(capitalize('hello')).toBe('Hello').message("Should work correctly")
        yield expect(capitalize('one \ntwo')).toBe('One \nTwo').message("Should work correctly")

    @test('parentesize')
    def _parentesize(self):
        yield expect(
            parentesize('1 + (3 + 8)')
        ).toBe(('1 + $', '3 + 8')).message("Should return set of 2, devided by open bracket")

        yield expect(
            parentesize('1 + 3')
        ).toBe(('1 + 3', None)).message("Should return set of 2, devided by open bracket")

        yield expect(
            parentesize('(b + c)')
        ).toBe(('$', 'b + c')).message("Should return set of 2, devided by open bracket")

        yield expect(lambda:parentesize('))')).toRaise(ValueError).message("Should raise ValueError")

    @test('split_by_first')
    def _split_by_first(self):
        yield expect(split_by_first('a', '+')).toFalse('Should return false if not found char')
        yield expect(split_by_first('a + b', '+')).toBe(
            ['+', 'a', 'b']
        ).message('Should work correct with single char')
        
        yield expect(split_by_first('a + b + c', '+')).toBe(
            ['+', 'a', 'b + c']
        ).message('Should work correct with double char')

    # @test('split_all_by')
    # def _split_all(self):
    #     def recursive():
    #         equality_case(split_all_by_recursive('a', '+'), 'a', 'Should work correct with simple strings')
    #         equality_case(split_all_by_recursive('a + b', '+'), ['+', 'a', 'b'], 'Should work correct with single char')
    #         equality_case(split_all_by_recursive('a + b + c', '+'), ['+', 'a', ['+', 'b', 'c']], 'Should work correct with double char')
    #     yield self.case(recursive)
