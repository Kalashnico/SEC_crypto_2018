#!/usr/bin/env python

import base64
import sys
import binascii
from Crypto.Cipher import AES


unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def read_file():
    file = open(sys.argv[1], 'rb')
    file_data = file.readlines()

    file_data[0] = file_data[0].rstrip()
    file_data[1] = file_data[1].rstrip()
    file_data[2] = file_data[2].rstrip()

    return file_data


def base64_to_hex(msg):
    return binascii.hexlify(binascii.a2b_base64(msg))


def hex_to_base64(msg):
    return binascii.b2a_base64(binascii.unhexlify(msg))


def xor_str(xs, ys):
    print("xs = " + xs)
    print("ys = " + ys)
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))


def ecb_decryption(key, msg):
    msg = base64.b64decode(msg)
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(msg))


def cbc_decryption(key, iv, msg):
    ct_list = [iv]
    ct_list += [msg[i:i + len(key)] for i in range(0, len(msg), len(key))]
    print("ct list = " + str(ct_list) + " len : " + str(len(ct_list)))
    pt_list = [xor_str(ecb_decryption(key, ct_list[i + 1]), ct_list[i]) for i in range(0, len(ct_list) - 1)]

    return ''.join(pt_list)


if __name__ == '__main__':

    try:
        file_data = read_file()
    except IOError:
        sys.exit(84)

    key = file_data[0]
    iv = file_data[1]
    msg = base64_to_hex(file_data[2]).decode('hex')
    print(cbc_decryption(key, iv, msg))
    sys.exit(0)