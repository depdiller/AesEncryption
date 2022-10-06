## Лабораторная работа №2

#### Описание утилиты:

```
usage: cipher [-h] [--version] -m {ecb,cbc} (-e | -d) -k KEY
              [-i IV] [-g]
              file

AES encryption util

positional arguments:
  file                  File with plaintext/cipher

optional arguments:
  -h, --help            show this help message and exit
  --version             Project version
  -m {ecb,cbc}, --mode {ecb,cbc}
                        Encryption/Decryption algorithm
  -e, --enc             Encryption mode
  -d, --dec             Decryption mode
  -k KEY, --key KEY     Key in hex
  -i IV, --iv IV        Initialization vector for CBC
                        algorithm
  -g, --debug           Debug mode: to display all
                        intermediate values
```

- Режимы: ECB, CBC
- Алгоритм блочного шифрования: SP-сеть 
- Информационный блок: 32 бита
- Размер ключа: 32 бита
- Количество раундов: 2