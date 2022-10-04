import binary_functions

def key_gen(key_zero: bytearray) -> list[bytearray]:
    key_list = []
    key_one = invert(key_zero)
    key_two = xor(key_zero, key_one)
    key_list.append(key_zero)
    key_list.append(key_one)
    key_list.append(key_two)
    return key_list
