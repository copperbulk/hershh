import struct

# Set our format as a signed integer, a float, and two booleans
data_format = '<if2?'

packed = struct.pack(data_format, 5000, 0.5, True, False)
print(packed)
# b'\x88\x13\x00\x00\x00\x00\x00?\x01\x00'

unpacked = struct.unpack(data_format, packed)
print(unpacked)
# (5000, 0.5, True, False)
