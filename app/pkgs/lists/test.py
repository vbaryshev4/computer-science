from pkgs.lists import * 
from pkgs.tester import *


class Tests(Suite):    
    module = "pkgs.lists"
    name = 'Lists Module Tests'
    description = 'Tests for module lists'

    @test('Shuffle test', 'shuffle')
    def shuffle_test():
        ints = [1,2,3,4,5,6,7]
        strs = ['a','b','c','d']
        mixed = [1, 2, 3, 'a', 'b','c']

        yield TestCase(
            'Shuffles a list with ints'
        ).expect(shuffle(ints))._not().to_be(ints)

        yield TestCase(
            'Shuffles a list with str'
        ).expect(shuffle(strs))._not().to_be(strs)
        
        yield TestCase(
            'Shuffles a list with mixed'
        ).expect(shuffle(mixed))._not().to_be(mixed)  

    @test('Chunk tests', 'chunk')
    def chunk_test():

        yield TestCase(
            'Divides list by two-step sub-lists'
        ).expect(
            chunk(list(range(10)), 2)
        ).to_be([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])    

        yield TestCase(
            'Devides list by three-step sub-lists'
        ).expect(
            chunk(list(range(10)), 3)
        ).to_be([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]])

        yield  TestCase(
            'Devides list by seven-step sub-lists'
        ).expect(
            chunk(list(range(10)), 7)
        ).to_be([[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]])

    @test('Get last item test', 'get_last_item')
    def get_last_item_test():

        yield TestCase(
            'Should work with 1-level list'
        ).expect(
            get_last_item([1,2,3])
        ).to_be(3)

        yield TestCase(
            'Should work with 2-level list'
        ).expect(
            get_last_item([1,2,[3,4]])
        ).to_be(4)

        yield TestCase(
            'Should work with 3-level list'
        ).expect(
            get_last_item([1,2,[[3]]])
        ).to_be(3)

    @test('Traverse recursive test', 'traverse_recursive')
    def traverse_recursive_test():

        yield TestCase(
            'Should traverse tree using a func. Test case: print()'
        ).expect(
            traverse_recursive([0,[1,[2,3,4]]], print)
        ).to_be([None, [None, [None, None, None]]])

        yield TestCase(
            'Should compose a list from tree values. NB: with print() in func'
        ).expect(
            traverse_recursive([1, [2, [3, [4]], 5]], print)
        ).to_be([1, 2, 3, 4, 5])

    @test('Drop test', 'drop')
    def drop_test():

        yield TestCase(
            'Should delete elems from list'
        ).expect(
            drop([1, 2, 3, 1, 2, 3, 1, 2, 3], [2, 3])
        ).to_be([1, 1, 1])

    @test('Uniq test', 'uniq')
    def uniq_test():

        yield TestCase(
            'Should collect only unique elements form list'
        ).expect(
            uniq([1, 2, 5, 2, 3, 3])
        ).to_be([1, 2, 5, 3])

    @test('From pairs test', 'from_pairs')
    def from_pairs_test():
        
        yield TestCase(
            'Should compose dict for list only with uniq keys'
        ).expect(
            from_pairs([['a', 1], ['b', 2], ['c', 3]])
        ).to_be({'a': 1, 'b': 2, 'c': 3})

    @test('Count test','count')
    def count_test():
        
        yield TestCase(
            'Should compose dict form list and count keys as values'
        ).expect(
            count(['a', 'a', 'b'])
        ).to_be({'a': 2, 'b': 1})

    @test('Pick test', 'pick')
    def pick_test():
        
        yield TestCase(
            'Should compose a new dict with keys in list'
        ).expect(
            pick({'a':10,'b':20,'c':30,'d': 40}, ['a', 'd'])
        ).to_be({'a':10,'d':40})

