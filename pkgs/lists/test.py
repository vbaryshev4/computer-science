from pkgs.lists import * 
from pkgs.tester import *

class ListTests(Suite):
    
    module = "pkgs.lists"

    def shuffle_test(self):
        non_equality_case(
            shuffle([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7], 
                'Shuffles a list with ints'
        )
        non_equality_case(
            shuffle(['a','b','c','d']), ['a','b','c','d'], 
                'Shuffles a list with str'
        )
        non_equality_case(
            shuffle([1,2,3,'a','b','c']), [1,2,3,'a','b','c'], 
                'Shuffles a list with mixed'
        )

    def chunk_test(self):
        equality_case(
            chunk(list(range(10)), 2), [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]], 
                "Devides list by two-step sub-lists"
        )
        equality_case(
            chunk(list(range(10)), 3), [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]],
                "Devides list by three-step sub-lists"
        )
        equality_case(
            chunk(list(range(10)), 7), [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]],
                "Devides list by seven-step sub-lists"
        )

    def get_last_item_test(self):
        equality_case(
            get_last_item([1,2,3]), 3, 'Should work with 1-level list'
        )
        equality_case(
            get_last_item([1,2,[3,4]]), 4, 'Should work with 2-level list'
        )
        equality_case(
            get_last_item([1,2,[[3]]]), 3, 'Should work with 3-level list'
        )

    def traverse_test(self):
        pass

    def flatten_test(self):
        pass

    def drop_test(self):
        pass

    def uniq(self):
        pass

    def from_pairs(self):
        pass

    def count(self):
        pass

    def pick(self):
        pass