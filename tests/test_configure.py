"""configure tests"""

import os
import unittest

from devicepilot.configure import configure


class TestConfigure(unittest.TestCase):
    """configure tests"""
    def test_get_explicit_api_key(self):
        """gets an explicit api key"""
        key = configure("the-key")
        self.assertEqual(key, "TOKEN the-key")

    def test_get_key_from_environment(self):
        """gets a key from the environment"""
        os.environ["DP_API_KEY"] = "here-is-a-key"
        key = configure()
        self.assertEqual(key, "TOKEN here-is-a-key")
        del os.environ["DP_API_KEY"]

    def test_normalises_token(self):
        """normalises TOKEN"""
        key = configure("ToKeN the-key")
        self.assertEqual(key, "TOKEN the-key")

    def test_raise_if_no_key(self):
        """raises if no key provided"""
        with self.assertRaises(ValueError):
            configure()

    def test_raise_if_blank_key(self):
        """raises if no blank provided"""
        with self.assertRaises(ValueError):
            configure("  ")
