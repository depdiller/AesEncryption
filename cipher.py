def invert(data: bytearray) -> bytearray:
    result = data[:]
    for index in range(len(result)):
        result[index] ^= 0xFF
    return result

def key_gen(key_zero: bytearray) -> list[bytearray]:
    key_list = []
    key_one = invert(key_zero)
    key_two = bytes(a ^ b for a, b in zip(key_zero, key_one))
    
    key_list.append(key_zero)
    key_list.append(key_one)
    key_list.append(key_two)
    return key_list
