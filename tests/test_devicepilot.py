"""post tests"""

import json
import unittest

import responses

import devicepilot


class TestDevicePilot(unittest.TestCase):
    """post tests"""
    @responses.activate
    def test_post_single_record(self):
        """posts a single record to DevicePilot"""
        responses.add(responses.POST, "https://api.devicepilot.com/devices", json={}, status=202)
        key = "abc"
        record = {"$id": "device-id", "temperature": 20, "orientation": "SOUTH"}
        devicepilot.post(record, key)
        self.assertEqual(responses.calls[0].request.headers["Authorization"], "TOKEN abc")
        _json = json.loads(responses.calls[0].request.body)
        self.assertEqual(_json, [record])

    @responses.activate
    def test_post_records(self):
        """posts records to DevicePilot"""
        responses.add(responses.POST, "https://api.devicepilot.com/devices", json={}, status=202)
        key = "def"
        records = [
            {"$id": "a", "colour": "blue"},
            {"$id": "b", "switchedOn": True},
            {"$id": "c", "temperature": 20, "orientation": "NORTH"}
        ]
        devicepilot.post(records, key)
        self.assertEqual(responses.calls[0].request.headers["Authorization"], "TOKEN def")
        _json = json.loads(responses.calls[0].request.body)
        self.assertEqual(_json, records)
