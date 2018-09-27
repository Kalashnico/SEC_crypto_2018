#!/usr/bin/env python3

import base64
import sys
from Crypto.Cipher import AES


unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def read_file():
    file = open(sys.argv[1], 'rb')
    file_data = file.readlines()
    file_data[0] = file_data[0].rstrip()
    file_data[1] = file_data[1].rstrip()
    file_data[2] = file_data[2].rstrip()

    return file_data


class AESCipher(object):

    def __init__(self, key):
        self.key = key.decode('hex')

    def decrypt(self, msg, iv_txt):
        msg = base64.b64decode(msg)
        iv = iv_txt[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(msg))


if __name__ == '__main__':

    file_data = read_file()
    cipher = AESCipher(file_data[0])

    decrypted_msg = cipher.decrypt(file_data[2], file_data[1])
    decrypted_msg = decrypted_msg.rstrip()
    print("%s" % decrypted_msg)
