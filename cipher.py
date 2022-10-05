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
        encrypted_block = aes.all_rounds_encryption(block, keys)
        encrypted_text.extend(encrypted_block)
    return encrypted_text

def cbc_encryption(data: str, key: str, iv: str):
    key = bytearray.fromhex(key)
    iv = bytearray.fromhex(iv)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    if (len(iv) != aes.BLOCK_SIZE):
        raise Exception('Initialization vector must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    encrypted_text = bytearray()
    xor_with = iv
    for block in blocks:
        xored_block = xor(xor_with, block)
        encrypted_block = aes.all_rounds_encryption(xored_block, keys)
        xor_with = encrypted_block
        encrypted_text.extend(encrypted_block)
    return encrypted_text
    
    
data = '02 5d 2a 1e 5f ff 1a 3b c3'
key = '12 34 6d 3b'
iv = '42 5b 3a 1f'
ecb_encrypted = ecb_encryption(data, key)
cbc_encrypted = cbc_encryption(data, key, iv)

print(ecb_encrypted.hex())
print(cbc_encrypted.hex())
