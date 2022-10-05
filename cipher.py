from key_generation import key_gen
from binary_functions import xor
import aes

def partitioning(data: str):
    data_bytes = bytearray.fromhex(data)
    length = len(data_bytes)
    number_of_blocks = length // aes.BLOCK_SIZE
    list_of_blocks = []
    for i in range(0, length, aes.BLOCK_SIZE):
        block = data_bytes[i:i + aes.BLOCK_SIZE]
        list_of_blocks.append(block)
    return list_of_blocks

def ecb_encryption(data: str, key: str):
    key = bytearray.fromhex(key)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    encrypted_text = bytearray()
    for block in blocks:
        # 0 round
        zero_round_res = xor(block, keys[0])
        # 1 round
        first_round_res = bytearray()
        for block in zero_round_res:
            encrypted_block = aes.encrypt_block(block, keys[1])
            first_round_res.extend(encrypted_block)
        # 2 round
        second_round_res = bytearray()
        for block in first_round_res:
            encrypted_block = aes.encrypt_block(block, keys[2])
            second_round_res.extend(encrypted_block)
        encrypted_text.extend(second_round_res)
    return encrypted_text

data = '02 5d 1a 3e 5f ff 1a 3b c3'
key = '12 34 6d 3b'
encrypted = ecb_encryption(data, key)
print(encrypted.hex())
