#!/usr/bin/env python3
'''test utils'''

from parameterized import parameterized
import unittest
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    '''test access_nested_map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        '''test access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
