import hashlib

def encodepass(str):
    m2 = hashlib.md5()
    m2.update(str.encode('utf-8'))
    return m2.hexdigest()