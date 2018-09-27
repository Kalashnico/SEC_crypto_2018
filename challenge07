#!/usr/bin/env python3.6

import base64
import sys
import binascii
from Crypto.Cipher import AES


unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def read_file():
    file = open(sys.argv[1], 'rb')
    file_data = file.readlines()
    file_data[0] = file_data[0].rstrip()
    return file_data


class AESCipher(object):

    def __init__(self, key):
        self.key = binascii.unhexlify(key)

    def decrypt(self, msg):
        msg = base64.b64decode(msg)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(msg))


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit(84)

    try:
        file_data = read_file()
    except IOError:
        sys.exit(84)

    cipher = AESCipher(file_data[0])

    decrypted_msg = cipher.decrypt(file_data[1])

    decrypted_msg = base64.b64encode(decrypted_msg)
    decrypted_msg = decrypted_msg.decode('utf-8').rstrip()
    print("%s" % decrypted_msg)
    sys.exit(0)