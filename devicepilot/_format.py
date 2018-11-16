"""Record formatting utilities"""

def flatten(nested, parent_key="", sep="."):
    """flatten a nested dict into a DevicePilot compatible namespaced-dict"""
    items = []
    for key, value in nested.items():
        new_key = parent_key + sep + str(key) if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            lst = list(value)
            dct = {k: v for k, v in enumerate(lst)}
            items.extend(flatten(dct, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

def format_record(record):
    """format a single record"""
    return flatten(record)

def _format(records):
    """format a list of records"""
    return list(map(format_record, records))
