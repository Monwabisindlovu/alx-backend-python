#!/usr/bin/env python3

"""
Test module for utils.memoize decorator.
"""

import unittest
from unittest.mock import patch, Mock
from utils import memoize, access_nested_map


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator.
    """

    class TestClass:
        """
        Test class with a_method and a_property decorated with memoize.
        """

        def a_method(self):
            """
            Method to be memoized.
            """
            return 42

        @memoize
        def a_property(self):
            """
            Property decorated with memoize, using a_method.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test method for the memoize decorator.
        Verifies that a_method is only called once when calling a_property
        twice.
        """
        test_instance = self.TestClass()

        # Mock a_method
        with patch.object(test_instance, 'a_method') as mock_a_method:
            # Call a_property twice
            result_1 = test_instance.a_property()
            result_2 = test_instance.a_property()

            # Check that a_method is only called once
            mock_a_method.assert_called_once()

            # Check that the results are correct
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)


if __name__ == "__main__":
    unittest.main()
