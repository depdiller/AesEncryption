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
    return encrypted_text.hex()

def ecb_decryption(data: str, key: str):
    key = bytearray.fromhex(key)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    decrypted_text = bytearray()
    for block in blocks:
        decrypted_block = aes.all_rounds_decryption(block, keys)
        decrypted_text.extend(decrypted_block)
    return decrypted_text.hex()

def cbc_decryption(data: str, key: str, iv: str):
    key = bytearray.fromhex(key)
    iv = bytearray.fromhex(iv)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    if (len(iv) != aes.BLOCK_SIZE):
        raise Exception('Initialization vector must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    decrypted_text = bytearray()
    xor_with = iv
    for block in blocks:
        decrypted_block = aes.all_rounds_decryption(block, keys)
        xored_block = xor(xor_with, decrypted_block)
        xor_with = block
        decrypted_text.extend(xored_block)
    return decrypted_text.hex()

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
    return encrypted_text.hex()
    
    
data = '025d2a1e5fff1a3bc3'
key = '11346d3b'
iv = '425b3a1f'
ecb_encrypted = ecb_encryption(data, key)
cbc_encrypted = cbc_encryption(data, key, iv)

ecb_decrypted = ecb_decryption(ecb_encrypted, key)
cbc_decrypted = cbc_decryption(cbc_encrypted, key, iv)
print(ecb_encrypted + ' ' + ecb_decrypted)
print(cbc_encrypted + ' ' + cbc_decrypted)

assert (
    ecb_decrypted == data
)
assert (
    cbc_decrypted == data
)
