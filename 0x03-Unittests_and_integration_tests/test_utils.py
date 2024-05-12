#!/usr/bin/env python3

"""
Tests for utils.py
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, message):
        """
        Test access_nested_map function raises KeyError
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), message)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class to test memoize decorator
    """

    class TestClass:
        """
        TestClass for memoization
        """

        def a_method(self):
            """
            Sample method
            """
            return 42

        @memoize
        def a_property(self):
            """
            Sample property with memoization
            """
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test memoize decorator
        """
        mock_a_method.return_value = 42
        obj = self.TestClass()
        self.assertEqual(obj.a_property, 42)
        self.assertEqual(obj.a_property, 42)
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
