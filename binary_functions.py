import itertools

def invert(data: bytearray) -> bytearray:
    result = data[::-1]
    for i in range(len(result)):
        result[i] = reverse_bit(result[i])
    return result

def reverse_bit(num):
    return int('{:08b}'.format(num)[::-1], 2)

def xor(a, b):
    len_a = len(a)
    len_b = len(b)
    if (len_a != len_b):
        if (len_a < len_b): 
            a, b = b, a
            len_a, len_b = len_b, len_a
        res = bytearray(a ^ b for a, b in zip(a[len_b::], b))
        for i in range(len_a - len_b):
            res.insert(i, a[i])
        return res
    else:  
        return bytearray(a ^ b for a, b in zip(a, b))

# 0011 1111b = 0x3f = 3 * 15 + 15 = 63
# -> 1111 1100 = 0xfc
byte = bytearray.fromhex('3f')
inv_bytes = invert(byte).hex()
assert inv_bytes == 'fc'

# 1010 1110 xor 0001 1001 = ae xor 19 = 1011 0111 = b7
byte1 = bytearray.fromhex('ae')
byte2 = bytearray.fromhex('19')
assert xor(byte1, byte2).hex() == 'b7'

# ffae xor b7
byte1 = bytearray.fromhex('ffae')
assert xor(byte1, byte2).hex() == 'ffb7'
assert xor(byte2, byte1).hex() == 'ffb7'