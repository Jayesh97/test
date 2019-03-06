import unittest
import merge_logic

class Testmerge(unittest.TestCase):

    def test_merge(self):
        result = merge_logic.merge('test1/dir1/input.yaml')
        self.assertEqual(result,{'color': 'blue', 'count': 2, 'size': 8})

        result = merge_logic.merge('test2/dir1/input.yaml')
        self.assertEqual(result,{'wishlist': ['worldpeace', 'car', 'pony']})

        result = merge_logic.merge('test3/dir1/input.yaml')
        self.assertEqual(result,{'todo': {'laundry': {'priority': 'low'}, 'dishes': {'priority': 'low'}, 'vacuum': {'priority': 'high'}}})


if __name__ == '__main__':
    unittest.main()