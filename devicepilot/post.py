"""Post device telemetry into DevicePilot"""

import requests

from ._format import _format
from .batch import batch
from .configure import configure
from .validate import validate

DEVICES_URL = "https://api.devicepilot.com/devices"

def post_batch(authorization, _batch):
    """Post a batch of records to DevicePilot"""
    headers = {"Authorization": authorization}
    response = requests.post(DEVICES_URL, headers=headers, json=_batch)
    if response.status_code != 202:
        raise ValueError("Failed to post records: " + response.text)

def post(records, apikey=None):
    """Post records into DevicePilot

    Keyword arguments:
    records -- either a single dict or list of dicts of device records as { $id, ...telemetry }
    apikey -- DevicePilot api key to use; taken from env DP_API_KEY if None (default None)
    """
    authorization = configure(apikey)
    validated = validate(records)
    formatted = _format(validated)
    batches = batch(formatted)
    for _batch in batches:
        post_batch(authorization, _batch)
