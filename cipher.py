import modes_algo
import argparse

parser = argparse.ArgumentParser(prog='cipher', description='AES encryption util')
parser.add_argument('--version', action='version', version='%(prog)s 1.0',
    help='Project version')
parser.add_argument('-m', '--mode', choices=['ecb', 'cbc'], required=True,
    help='Encryption/Decryption algorithm')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--enc', action='store_true', help='Encryption mode')
group.add_argument('-d', '--dec', action='store_true', help='Decryption mode')
parser.add_argument('-k', '--key', required=True, help='Key in hex')
parser.add_argument('-i', '--iv', 
    help='Initialization vector for CBC algorithm')
parser.add_argument('-g', '--debug', action='store_true',
    help='Debug mode: to display all intermediate values')
parser.add_argument('file',
    help='File with plaintext/cipher')

args = parser.parse_args()
mode = args.mode
file_path = args.file
key = args.key
iv = args.iv
if mode == 'cbc' and iv == None:
    raise Exception('Must provide iv in CBC algorithm')
debug = args.debug
with open(file_path, 'r') as input_file:
    text = input_file.readline().rstrip('\n')
    res = None
    if args.enc == True:
        if mode == 'cbc': 
            res = modes_algo.cbc_encryption(text, key, iv, debug)
        elif mode == 'ecb': 
            res = modes_algo.ecb_encryption(text, key, debug)
    elif args.dec == True:
        if mode == 'cbc':
            res = modes_algo.cbc_decryption(text, key, iv, debug)
        elif mode == 'ecb': 
            res = modes_algo.ecb_decryption(text, key, debug)
    print(res)