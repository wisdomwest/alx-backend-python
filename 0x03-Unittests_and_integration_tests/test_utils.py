#!/usr/bin/env python3
'''test utils'''

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)


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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''test access_nested_map exception'''
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), f"'{expected}'")


class TestGetJson(unittest.TestCase):
    '''test get_json'''

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url, expected):
        '''test get_json'''
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected
            self.assertEqual(get_json(test_url), expected)
            mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    '''test memoize'''
    def test_memoize(self):
        '''test memoize'''
        class TestClass:
            '''test class'''
            def a_method(self):
                '''a method'''
                return 42

            @memoize
            def a_property(self):
                '''a property'''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock.assert_called_once()
