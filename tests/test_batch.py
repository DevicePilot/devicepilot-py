"""batch tests"""

import unittest

from devicepilot.batch import batch


class TestBatch(unittest.TestCase):
    """batch tests"""
    def test_split_array_into_chunks(self):
        """should split list into chunks of 100"""
        records = list(range(345))
        batches = batch(records)
        self.assertEqual(batches.__len__(), 4)
        self.assertEqual(batches[0].__len__(), 100)
        self.assertEqual(batches[0][99], 99)
        self.assertEqual(batches[1].__len__(), 100)
        self.assertEqual(batches[1][99], 199)
        self.assertEqual(batches[2].__len__(), 100)
        self.assertEqual(batches[2][99], 299)
        self.assertEqual(batches[3].__len__(), 45)
        self.assertEqual(batches[3][44], 344)
