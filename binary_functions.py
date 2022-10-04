def invert(data: bytearray) -> bytearray:
    result = data[:]
    for index in range(len(result)):
        result[index] ^= 0xFF
    return result

def xor(a, b):
    return bytearray(bytes(a ^ b for a, b in zip(key_zero, key_one)))