"""Record batching utilities"""

BATCH_SIZE = 100

def chunks(lst, chunk_size):
    """Split a list into chunks of length n"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i+chunk_size]

def batch(records):
    """Batch records into post-able chunks"""
    return list(chunks(records, BATCH_SIZE))
