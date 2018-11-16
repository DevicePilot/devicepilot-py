"""_format tests"""

import unittest

from devicepilot._format import _format


class TestFormat(unittest.TestCase):
    """_format tests"""
    def test_format_array_into_flat_devicepilot_json(self):
        """formats a list of records in flat DevicePilot JSON"""
        records = [
            {"$id": "1", "nested": {"property": "a"}, "simple": 2},
            {"$id": "2", "array": [{"something": "b"}, "c"], "simple": False},
        ]
        formatted = _format(records)
        self.assertEqual(formatted, [
            {
                "$id": "1",
                "nested.property": "a",
                "simple": 2
            },
            {
                "$id": "2",
                "array.0.something": "b",
                "array.1": "c",
                "simple": False
            }
        ])
