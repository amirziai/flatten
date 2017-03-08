import unittest

from flatten_json import flatten, unflatten, unflatten_list
from util import check_if_numbers_are_consecutive


class UnitTests(unittest.TestCase):
    def test_numbers_consecutive(self):
        """Checks if all numbers in a list are consecutive integers"""
        list_ = [1, 2, 3, 4, 5]
        actual = check_if_numbers_are_consecutive(list_)
        self.assertTrue(actual)

        list_ = [0, 1, 5]
        actual = check_if_numbers_are_consecutive(list_)
        self.assertFalse(actual)

        list_ = [1.0, 2.0, 3.0]
        actual = check_if_numbers_are_consecutive(list_)
        self.assertTrue(actual)

        list_ = range(10)
        actual = check_if_numbers_are_consecutive(list_)
        self.assertTrue(actual)

        list_ = range(10, 0, -1)
        actual = check_if_numbers_are_consecutive(list_)
        self.assertFalse(actual)

    def test_no_flatten(self):
        dic = {'a': '1', 'b': '2', 'c': 3}
        expected = dic
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_one_flatten(self):
        dic = {'a': '1',
               'b': '2',
               'c': {'c1': '3', 'c2': '4'}
               }
        expected = {'a': '1', 'b': '2', 'c_c1': '3', 'c_c2': '4'}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_custom_separator(self):
        dic = {'a': '1',
               'b': '2',
               'c': {'c1': '3', 'c2': '4'}
               }
        expected = {'a': '1', 'b': '2', 'c*c1': '3', 'c*c2': '4'}
        actual = flatten(dic, '*')
        self.assertEqual(actual, expected)

    def test_list(self):
        dic = {
            'a': 1,
            'b': [{'c': [2, 3]}]
        }
        expected = {'a': 1, 'b_0_c_0': 2, 'b_0_c_1': 3}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_list_and_dict(self):
        dic = {
            'a': 1,
            'b': 2,
            'c': [{'d': [2, 3, 4], 'e': [{'f': 1, 'g': 2}]}]
        }
        expected = {'a': 1, 'b': 2, 'c_0_d_0': 2, 'c_0_d_1': 3, 'c_0_d_2': 4, 'c_0_e_0_f': 1, 'c_0_e_0_g': 2}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_blog_example(self):
        dic = {
            "a": 1,
            "b": 2,
            "c": [{"d": ['2', 3, 4], "e": [{"f": 1, "g": 2}]}]
        }
        expected = {'a': 1, 'b': 2, 'c_0_d_0': '2', 'c_0_d_1': 3, 'c_0_d_2': 4, 'c_0_e_0_f': 1,
                    'c_0_e_0_g': 2}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_unflatten_no_list(self):
        dic = {
            'a': 1,
            'b_a': 2,
            'b_b': 3,
            'c_a_b': 5
        }
        expected = {
            'a': 1,
            'b': {'a': 2, 'b': 3},
            'c': {'a': {'b': 5}}
        }
        actual = unflatten(dic)
        self.assertEqual(actual, expected)

    def test_unflatten_with_list(self):
        """Dictionary with lists"""
        dic = {
            'a': 1,
            'b_0': 1,
            'b_1': 2,
            'c_a': 'a',
            'c_b_0': 1,
            'c_b_1': 2,
            'c_b_2': 3
        }
        expected = {
            'a': 1,
            'b': [1, 2],
            'c': {'a': 'a', 'b': [1, 2, 3]}
        }
        actual = unflatten_list(dic)
        self.assertEqual(actual, expected)

        dic = {'a': 1, 'b_0': 5}
        expected = {'a': 1, 'b': [5]}
        actual = unflatten_list(dic)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
