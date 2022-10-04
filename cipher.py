import key_gen
import aes

def partitioning(data: str):
    data_bytes = bytearray.fromhex(data)
    length = len(data_bytes)
    number_of_blocks = length // BLOCK_SIZE
    list_of_blocks = []
    for i in range(0, length, BLOCK_SIZE):
        block = data_bytes[i:i + BLOCK_SIZE]
        list_of_blocks.append(block)
    return list_of_block

def encryption(data: str, key: str):
    key = bytearray.fromhex(key)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    # 0 round
    zero_round_res = xor(blocks, keys[0])
    # 1 round
    first_round_res = bytearray()
    for block in zero_round_res:
        encrypted_block = encrypt_block(block, key[1])
        first_round_res.extend(encrypted_block)
    # 2 round
    second_round_res = bytearray()
    for block in first_round_res:
        encrypted_block = encrypt_block(block, key[2])
        second_round_res.extend(encrypted_block)
    return second_round_res
