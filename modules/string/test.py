from modules.string import *
from modules.tester import *

equality_case(trim('  a'), 'a', 'Should trim spaces from start of string')
equality_case(trim('a   '), 'a', 'Should trim spaces from end of string')

equality_case(kebabToSnake("kabeab-to-snake"), 'kabeab_to_snake', 'Should change all - to _')
equality_case(kebabToCamel("kabeab-to-camel"), 'kabeabToCamel', 'Should return camelCase string')

equality_case(parentes("1+(2+3)"), (2, "2+3"), "Should work correctly")
equality_case(parentes("1+3"), None, "Should return None if not found")

equality_case(count("(((", "("), (3), "Should work correctly") 
equality_case(count("+-+++--", "+"), (4), "Should work correctly") 
equality_case(count("aAaAAA", "a"), (2), "Should work correctly") 
equality_case(count("?###!%", "?"), (1), "Should work correctly") 
equality_case(count("?###!%", "#"), (3), "Should work correctly") 
