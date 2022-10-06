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

def ecb_encryption(data: str, key: str, debug):
    key = bytearray.fromhex(key)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    encrypted_text = bytearray()
    for i, block in enumerate(blocks):
        if (i == len(blocks) - 1):
            block = aes.padding(block)
        encrypted_block = aes.all_rounds_encryption(block, keys)
        encrypted_text.extend(encrypted_block)
        if debug:
            print('%d block: %s -> (enc) -> %s' % (i, block.hex(), encrypted_block.hex()))
    return encrypted_text.hex()

def ecb_decryption(data: str, key: str, debug):
    key = bytearray.fromhex(key)
    if (len(key) != aes.BLOCK_SIZE):
        raise Exception('Key must be 32 bits')
    keys = key_gen(key)
    blocks = partitioning(data)
    decrypted_text = bytearray()
    for i, block in enumerate(blocks):
        decrypted_block = aes.all_rounds_decryption(block, keys)
        decrypted_text.extend(decrypted_block)
        if debug:
            print('%d block: %s -> (dec) -> %s' % (i, block.hex(), decrypted_block.hex()))
    decrypted_text = aes.delete_padding(decrypted_text)
    return decrypted_text.hex()

def cbc_decryption(data: str, key: str, iv: str, debug):
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
    for i, block in enumerate(blocks):
        decrypted_block = aes.all_rounds_decryption(block, keys)
        xored_block = xor(xor_with, decrypted_block)
        xor_with = block
        decrypted_text.extend(xored_block)
        if debug:
            print('%d block: %s -> (dec) -> %s' % (i, block.hex(), decrypted_block.hex()))
    decrypted_text = aes.delete_padding(decrypted_text)
    return decrypted_text.hex()

def cbc_encryption(data: str, key: str, iv: str, debug):
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
    for i, block in enumerate(blocks):
        if (i == len(blocks) - 1):
            block = aes.padding(block)
        xored_block = xor(xor_with, block)
        encrypted_block = aes.all_rounds_encryption(xored_block, keys)
        xor_with = encrypted_block
        encrypted_text.extend(encrypted_block)
        if debug:
            print('%d block: %s -> (enc) -> %s' % (i, block.hex(), encrypted_block.hex()))
    return encrypted_text.hex()
    
data = '025d2a1e5fff1a3b12ab3e'
key = '11346d3b'
iv = '425b3a1f'
ecb_encrypted = ecb_encryption(data, key, False)
cbc_encrypted = cbc_encryption(data, key, iv, False)

ecb_decrypted = ecb_decryption(ecb_encrypted, key, False)
cbc_decrypted = cbc_decryption(cbc_encrypted, key, iv, False)

assert (
    ecb_decrypted == data
)
assert (
    cbc_decrypted == data
)
