# To represent string:
# Python3: bytes & str
#   bytes: Raw 8-bit values
#   str  : Contain unicode chars
# Python2: bytes & str
#   unicode: Unicode chars
#   str    : Raw 8-bit values
# -------------------
# Python2  |  Python3
# unicode  |  str
#   str    |  bytes

# Python3: bytes -> str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str 
    return value
# str -> bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str 
    return value

# Python2: bytes -> str
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

# str -> bytes    
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value

# Python3: bytes & str cannot be used together with '+' or '>', but you can do on unicode & str in Python2    
# open file with permission, need 'b' to write binary (bytes) in python3
# 'w' is only default on 'str' type in python3
# with open('somefile.bin', 'w') as f: # This won't work in python3
with open('somefile.bin', 'wb') as f:
    f.write(os.urandom(10))
