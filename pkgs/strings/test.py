import sys 

from pkgs.tester import * 
from pkgs.strings import *

class StringTest(Suite):
    
    module = "pkgs.strings"

    def index_of_test(self):
        equality_case(
            index_of(" qwe rty", "y"), 7, 'Should find index of element'

        )

    def parentes_test(self):
        equality_case(
            parentes("1+(2+3)"), (2, "2+3"), 
                "Should work correctly"
        )
        equality_case(
            parentes("1+3"), (-1, None), 
                "Should return None if not found"
        )
        error_case(
            lambda:parentes('('), 
                'Should raise ValueError on invalid expression'
        )

    def substring_test(self):
        equality_case(
            count("(((", "("), (3), 
                "Should work correctly"
        ) 
        equality_case(
            count("+-+++--", "+"), (4),
                "Should work correctly"
        ) 
        equality_case(
            count("aAaAAA", "a"), (2),
                "Should work correctly"
        ) 
        equality_case(
            count("?###!%", "?"), (1),
                "Should work correctly"
        ) 
        equality_case(
            count("?###!%", "#"), (3), 
                "Should work correctly"
        )
    
    def count_test(self):
        equality_case(
            count("qwe rty qwe rty", "q"), 2, 
                "Should count chars"

        )   
        
    def trim_test(self):
        equality_case(
            trim(''), '', 
                'Should work with empty string'
        )
        equality_case(
            trim('  a'), 'a', 
                'Should trim spaces from start of string'
        )
        equality_case(
            trim('a   '), 'a', 
                'Should trim spaces from end of string'
        )
        equality_case(
            trim('   a   '), 'a', 
                'Should trim spaces from start & end of string'
        )

    def split_by_first_test(self):
        equality_case(
            split_by_first('a', '+'), False, 
                'Should return false if not found char'
        )
        equality_case(
            split_by_first('a + b', '+'), ['+', 'a', 'b'], 
                'Should work correct with single char'
        )
        equality_case(
            split_by_first('a + b + c', '+'), ['+', 'a', 'b + c'], 
                'Should work correct with double char'
        )

    def split_all_by_test(self):
        equality_case(
            split_all_by('a', '+'), 'a', 
                'Should work correct with simple strings'
        )
        equality_case(
            split_all_by('a + b', '+'), ['+', 'a', 'b'], 
                'Should work correct with single char'
        )
        equality_case(
            split_all_by('a + b + c', '+'), ['+', 'a', ['+', 'b', 'c']], 
                'Should work correct with double char'
        )    

    def replace_test(self):
        equality_case(
            replace(" qwe rty ", "q", "Q"), ' Qwe rty ',
                "Should change char to a new char in string"
        )


    def kebab_test(self):
        equality_case(
            kebab_to_snake("kabeab-to-snake"), 'kabeab_to_snake', 
                'Should change all - to _'
        )
        equality_case(
            kebab_to_camel("kabeab-to-camel"), 'kabeabToCamel', 
                'Should return camelCase string'
        )

    def capitalize_test(self):
        equality_case(
            capitalize('this is my world'),('This Is My World'), 
                "Should work correctly"
        )
        equality_case(
            capitalize('hello'),('Hello'), 
                "Should work correctly"
        )
        equality_case(
            capitalize('one \ntwo'),('One \nTwo'),
                "Should work correctly"
        )

    def parentesize_test(self):
        equality_case(
            parentesize('1 + (3 + 8)'), ('1 + $', '3 + 8'), 
                "Should return set of 2, devided by open bracket"
        )
        equality_case(
            parentesize('1 + 3'), ('1 + 3', None), 
                "Should return set of 2, devided by open bracket"
        )
        equality_case(
            parentesize('(b + c)'), ('$', 'b + c'), 
                "Should return set of 2, devided by open bracket"
        )
        error_case(
            lambda:parentesize('))'), 
                "Should raise ValueError"
        )

    def interpolate_test(self):
        equality_case(
            interpolate('{a} {b}', {'a': 'Hello','b': 'World'}), 'Hello World',
                "Should interpolate string"
        )

    def full_replace_test(self):
        equality_case(
            full_replace("qwe rty", "qwe", "rty"), 'rty rty',
                "Should change string from tuple"
        )

    def parse_test(self):
        equality_case(
            parse('1 + 2 - 3 * 4'), ['+', 1, ['-', 2, ['*', 3, 4]]],
                "Should parce a string by math symbols in to lists"

        )

    