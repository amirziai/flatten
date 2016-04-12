import unittest

from flatten import flatten_json

class UnitTests(unittest.TestCase):
    def test_no_flatten(self):
        dic = {'a': '1', 'b': '2', 'c': 3}
        assert 3 == len(flatten_json(dic))


    def test_one_flatten(self):
        dic = {'a': '1',
                 'b': '2',
                 'c': {'c1': '3', 'c2': '4'}
                }
        assert 4 == len(flatten_json(dic))


    def test_one_flatten_keys(self):
        dic = {'a': '1',
                 'b': '2',
                 'c': {'c1': '3', 'c2': '4'}
                }
        keys = ['a', 'b', 'c_c1', 'c_c2']
        self.assertItemsEqual(keys, flatten_json(dic).keys())


    def test_three_flatten(self):
        dic = {
            'a': 1,
            'b': 2,
            'c': [{'d': [2, 3, 4], 'e': [{'f': 1, 'g': 2}]}]
        }
        flattened = flatten_json(dic)
        keys = ['a', 'b', 'c_0_e_0_g', 'c_0_e_0_f', 'c_0_d_1', 'c_0_d_0', 'c_0_d_2']

        assert 7 == len(flattened)
        self.assertItemsEqual(keys, flattened.keys())


if __name__ == '__main__':
    unittest.main()