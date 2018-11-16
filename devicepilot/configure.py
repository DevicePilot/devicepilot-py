"""DevicePilot module configuration utilities"""

import os
import re


def configure(apikey=None):
    """Get the configured api key"""
    key = ""
    if isinstance(apikey, str):
        key = apikey
    elif "DP_API_KEY" in os.environ:
        key = os.environ["DP_API_KEY"]
    normalised = re.sub(r"^TOKEN ", "", key, flags=re.IGNORECASE).strip()
    if normalised.__len__() == 0:
        raise ValueError(
            "API key must be provided either as apikey argument in `post`" \
            " or as DP_API_KEY environmental variable")
    return "TOKEN " + normalised
