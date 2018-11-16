"""Record validation utilities"""

def validate_record(record, index):
    """Validates a single record"""
    prefix = "Record[" + str(index) + "]"
    if not isinstance(record, dict):
        raise TypeError(prefix + " must be a dict")
    if "$id" not in record or \
        not isinstance(record["$id"], str) or \
        not record["$id"].strip().__len__() > 0:
        raise ValueError(prefix + " must include a $id to identify the device")

def validate(records):
    """Validate records to DevicePilot standard"""
    record_list = records
    if not isinstance(record_list, list):
        record_list = [records]
    for i, record in enumerate(record_list):
        validate_record(record, i)
    if record_list.__len__() == 0:
        raise ValueError("At least one record must be provided")
    return record_list
