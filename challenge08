#!/usr/bin/env python3.6

import sys
import codecs
import base64


def read_file():
    file = open(sys.argv[1], 'r')
    file_data = file.readlines()

    return file_data


def detect_ecb(txt):
    txt_cpy = str(txt)
    chunks = [txt_cpy[i:i+16*2] for i in range(0, len(txt_cpy), 16*2)]
    return not (len(set(chunks)) == len(chunks))


def convert_to_hex(txt):
    decoded = base64.b64decode(txt)
    hexa = codecs.encode(decoded, 'hex')
    return hexa.decode('utf-8').strip()


if __name__=='__main__':
    if len(sys.argv) != 2:
        sys.exit(84)

    try:
        file_data = read_file()
    except IOError:
        sys.exit(84)

    for i in range(0, len(file_data)):
        hex_txt = convert_to_hex(file_data[i])
        if detect_ecb(hex_txt):
            print(str(i + 1))

    sys.exit(0)
