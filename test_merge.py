import unittest
import merge_logic

class Testmerge(unittest.TestCase):

    #Best_practice - Test cases can be read from a CSV file   
    def test_merge(self):
        result = merge_logic.merge('testcases/test1/dir1/input.yaml')
        self.assertEqual(result,{'color': 'blue', 'count': 2, 'size': 9})

        result = merge_logic.merge('testcases/test2/dir1/input.yaml')
        self.assertEqual(result,{'wishlist': ['worldpeace', 'car', 'pony1']})

        result = merge_logic.merge('testcases/test3/dir1/input.yaml')
        self.assertEqual(result,{'todo': {'laundry': {'priority': 'low'}, 'dishes': {'priority': 'low'}, 'vacuum': {'priority': 'high'}}})


if __name__ == '__main__':
    unittest.main()
