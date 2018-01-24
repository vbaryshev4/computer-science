from pkgs.lists import * 
from pkgs.tester import *

class Tests(Suite):    
    module = "pkgs.lists"

    @test('Shuffle test', 'shuffle')
    def shuffle_test():
        ints = [1,2,3,4,5,6,7]
        strs = ['a','b','c','d']
        mixed = [1, 2, 3, 'a', 'b','c']

        yield Testcase(
            'Shuffles a list with ints'
        ).expect(shuffle(ints)).not_to_be(ints)

        yield Testcase(
            'Shuffles a list with str'
        ).expect(shuffle(strs)).not_to_be(strs)
        
        yield Testcase(
            'Shuffles a list with mixed'
        ).expect(shuffle(mixed)).not_to_be(mixed)
        

    # def chunk_test(self):
    #     equality_case(
    #         chunk(list(range(10)), 2), [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]], 
    #             "Devides list by two-step sub-lists"
    #     )
    #     equality_case(
    #         chunk(list(range(10)), 3), [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]],
    #             "Devides list by three-step sub-lists"
    #     )
    #     equality_case(
    #         chunk(list(range(10)), 7), [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]],
    #             "Devides list by seven-step sub-lists"
    #     )

    # def get_last_item_test(self):
    #     equality_case(
    #         get_last_item([1,2,3]), 3, 'Should work with 1-level list'
    #     )
    #     equality_case(
    #         get_last_item([1,2,[3,4]]), 4, 'Should work with 2-level list'
    #     )
    #     equality_case(
    #         get_last_item([1,2,[[3]]]), 3, 'Should work with 3-level list'
    #     )

    # def traverse_recursive_test(self):
    #     equality_case(
    #         traverse_recursive([0,[1,[2,3,4]]], print),[None, [None, [None, None, None]]],
    #             "Should traverse tree using a func. Test case: print()"
    #     )

    # def flatten_recursive_test(self):
    #     equality_case(
    #         flatten_recursive([1, [2, [3, [4]], 5]]), [1, 2, 3, 4, 5],
    #             "Should compose a list from tree values. NB: with print() in func"
    #     )

    # def drop_test(self):
    #     equality_case(
    #         drop([1, 2, 3, 1, 2, 3, 1, 2, 3], [2, 3]), [1, 1, 1],
    #             "Should delete elems from list"
    #     )

    # def uniq_test(self):
    #     equality_case(
    #         uniq([1, 2, 5, 2, 3, 3]), [1, 2, 5, 3],
    #             "Should collect only unique elements form list"
    #     )

    # def from_pairs_test(self):
    #     equality_case(
    #         from_pairs([['a', 1], ['b', 2], ['c', 3]]), {'a': 1, 'b': 2, 'c': 3},
    #             "Should compose dict for list only with uniq keys"
    #     )

    # def count_test(self):
    #     equality_case(
    #         count(['a', 'a', 'b']), {'a': 2, 'b': 1},
    #             "Should compose dict form list and count keys as values"
    #     )

    # def pick_test(self):
    #     equality_case(
    #         pick({'a':10,'b':20,'c':30,'d': 40}, ['a', 'd']), {'a':10,'d':40},
    #             "Should compose a new dict with keys in list"
    #     )



        