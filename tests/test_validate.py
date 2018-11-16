"""validate tests"""

import unittest

from devicepilot.validate import validate


class TestValidate(unittest.TestCase):
    """validate tests"""
    def test_normalises_records_to_list(self):
        """normalises "records" into a list"""
        records = [
            {"$id": "a", "aProperty": 1},
            {"$id": "b", "aProperty": 2},
        ]
        single = validate(records[0])
        self.assertEqual(single, [records[0]])
        lst = validate(records)
        self.assertEqual(lst, records)

    def test_enforces_records_as_dicts(self):
        """enforces records as dicts"""
        with self.assertRaises(TypeError):
            record = "not-a-record"
            validate(record)

    def test_enforces_records_as_non_empty(self):
        """enforces records cannot be an empty list"""
        with self.assertRaises(ValueError):
            validate([])

    def test_enforces_records_as_dict_with_string_id(self):
        """enforces records as dict with string $id"""
        with self.assertRaises(ValueError):
            record = {"hello": "world"}
            validate(record)
