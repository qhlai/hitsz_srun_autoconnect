
import hashlib
def _encode(value):
    return hashlib.sha1(value.encode()).hexdigest()
