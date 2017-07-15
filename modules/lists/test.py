from modules.lists import * 
from modules.tester import * 

class ListTests(Suite):
    @test('shuffle')
    def shuffle_tests(self):
        yield self.expect(
            shuffle([1,2,3,4,5,6,7])
        ).notToBe([1,2,3,4,5,6,7]).message('Shuffles a list with ints')

        yield self.expect(
            shuffle(['a','b','c','d'])
        ).notToBe(['a','b','c','d']).message('Shuffles a list with str')

        yield self.expect(
            shuffle([1,2,3,'a','b','c'])
        ).notToBe([1,2,3,'a','b','c']).message('Shuffles a list with mixed')

    @test('chunk')
    def chunk_tests(self):
        yield self.expect(
            chunk(list(range(10)), 2)
        ).toBe(
            [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
        ).message("Devides list by two-step sub-lists")

        yield self.expect(
            chunk(list(range(10)), 3)
        ).toBe(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
        ).message("Devides list by three-step sub-lists")

        yield self.expect(
            chunk(list(range(10)), 7)
        ).toBe(
            [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9]]
        ).message("Devides list by seven-step sub-lists")