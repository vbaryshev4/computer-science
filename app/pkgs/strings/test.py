from pkgs.strings import *
from pkgs.tester import * 

class Tests(Suite):
    module = "pkgs.strings"
    name = 'Strings Module Tests'
    description = 'Tests for module strings'

    @test('Index of test', 'index_of')
    def index_of_test():
        yield TestCase(
            'Should find index of element'
        ).expect(
            index_of(" qwe rty", "y")
        ).to_be(7)    

    
    @test('Substring test', 'substring_test')
    def substring_test():
        
        yield TestCase(
            'Should work correctly'
        ).expect(
            count("+-+++--", "+")
        ).to_be(4)

        yield TestCase(
            'Should work correctly'
        ).expect(
            count("aAaAAA", "a")
        ).to_be(2) 

        yield TestCase(
            'Should work correctly'
        ).expect(
            count("?###!%", "?")
        ).to_be(1)
    
        yield TestCase(
            'Should work correctly'
        ).expect(
            count("?###!%", "#")
        ).to_be(3) 

    @test('Count test', 'count_test')
    def count_test():
        
        yield TestCase(
            'Should count chars'
        ).expect(
            count("qwe rty qwe rty", "q")
        ).to_be(2)

    @test('Trim test', 'trim_test')
    def trim_test():
        
        yield TestCase(
            'Should work with empty string'
        ).expect(
            trim('')
        ).to_be('')     

        yield TestCase(
            'Should trim spaces from end of string'
        ).expect(
            trim('a   ')
        ).to_be('a')
    
        yield TestCase(
            'Should trim spaces from start & end of string'
        ).expect(
            trim('   a   ')
        ).to_be('a')

    @test('Split by first', 'split_by_first_test')
    def split_by_first_test():
        
        yield TestCase(
            'Should return false if not found char'
        ).expect(
            split_by_first('a', '+')
        ).to_be(False)     

        yield TestCase(
            'Should work correct with single char'
        ).expect(
            split_by_first('a + b', '+')
        ).to_be(['+', 'a', 'b'])

        yield TestCase(
            'Should work correct with double char'
        ).expect(
            split_by_first('a + b + c', '+')
        ).to_be(['+', 'a', 'b + c'])
    
    @test('Split all by', 'split_all_by_test')
    def split_all_by_test():
        
        yield TestCase(
            'Should work correct with simple strings'
        ).expect(
            split_all_by('a', '+')
        ).to_be('a')

        yield TestCase(
            'Should work correct with single char'
        ).expect(
            split_all_by('a + b', '+')
        ).to_be(['+', 'a', 'b'])     
        
        yield TestCase(
            'Should work correct with double char'
        ).expect(
            split_all_by('a + b + c', '+')
        ).to_be(['+', 'a', ['+', 'b', 'c']])


    @test('Replace test', 'replace_test')
    def replace_test():
        
        yield TestCase(
            'Should change char to a new char in string'
        ).expect(
            replace(" qwe rty ", "q", "Q")
        ).to_be(' Qwe rty ')     
    

    @test('Kebab test', 'kebab_test')
    def kebab_test():
        
        yield TestCase(
            'Should change all - to _'
        ).expect(
            kebab_to_snake("kabeab-to-snake")
        ).to_be('kabeab_to_snake')
        
        yield TestCase(
            'Should return camelCase string'
        ).expect(
            kebab_to_camel("kabeab-to-camel")
        ).to_be('kabeabToCamel') 

    @test('Capitalize test', 'capitalize_test')
    def capitalize_test():
        
        yield TestCase(
            'Should work correctly'
        ).expect(
            capitalize('this is my world')
        ).to_be('This Is My World')     

        yield TestCase(
            'Should work correctly'
        ).expect(
            capitalize('hello')
        ).to_be('Hello')

        yield TestCase(
            'Should work correctly'
        ).expect(
            capitalize('one \ntwo')
        ).to_be('One \nTwo')
    
    @test('Interpolate test', 'interpolate_test')
    def interpolate_test():
        
        yield TestCase(
            'Should interpolate string'
        ).expect(
            interpolate('{a} {b}', {'a': 'Hello','b': 'World'})
        ).to_be('Hello World')     


    @test('Full replace', 'full_replace_test')
    def full_replace_test():
        
        yield TestCase(
            'Should change string from tuple'
        ).expect(
            full_replace("qwe rty", "qwe", "rty")
        ).to_be('rty rty')

    @test('Parse', 'parse_test')
    def parse_test():
        
        yield TestCase(
            'Should parce a string by math symbols in to lists'
        ).expect(
            parse('1 + 2 - 3 * 4')
        ).to_be(['+', 1, ['-', 2, ['*', 3, 4]]])