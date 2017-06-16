#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def test_one_flatten_utf8(self):
        dic = {'a': '1',
               'ñ': 'áéö',
               'c': {'c1': '3', 'c2': '4'}
               }
        expected = {'a': '1', 'ñ': 'áéö', 'c_c1': '3', 'c_c2': '4'}
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

        dic = {'a': 1, 'b:0': 5}
        expected = {'a': 1, 'b': [5]}
        actual = unflatten_list(dic, ':')
        self.assertEqual(actual, expected)

    def test_unflatten_with_list_custom_separator(self):
        """Complex dictionary with lists"""
        dic = {
            'a:b': 'str0',
            'c:0:d:0:e': 'str1',
            'c:1:d:0:e': 'str4',
            'c:1:f': 'str5',
            'c:0:f': 'str2',
            'c:1:g': 'str6',
            'c:0:g': 'str3',
            'h:d:0:e': 'str7',
            'h:i:0:f': 'str8',
            'h:i:0:g': 'str9'
        }
        expected = {
            'a': {'b': 'str0'},
            'c': [
                {
                    'd': [{'e': 'str1'}],
                    'f': 'str2',
                    'g': 'str3'
                }, {
                    'd': [{'e': 'str4'}],
                    'f': 'str5',
                    'g': 'str6'
                }
            ],
            'h': {
                'd': [{'e': 'str7'}],
                'i': [{'f': 'str8', 'g': 'str9'}]
            }
        }
        actual = unflatten_list(dic, ':')
        self.assertEqual(actual, expected)

    def test_flatten_ignore_keys(self):
        """Ignore a set of root keys for processing"""
        dic = {
            'a': {'a': [1, 2, 3]},
            'b': {'b': 'foo', 'c': 'bar'},
            'c': {'c': [{'foo': 5, 'bar': 6, 'baz': [1, 2, 3]}]}
        }
        expected = {
            'a_a_0': 1,
            'a_a_1': 2,
            'a_a_2': 3
        }
        actual = flatten(dic, root_keys_to_ignore={'b', 'c'})
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
