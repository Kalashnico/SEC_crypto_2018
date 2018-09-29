#!/usr/bin/env python3.6

import sys
import binascii


def read_file():
    file_open = open(sys.argv[1], "r")

    try:
        file_data = file_open.readlines()
    except UnicodeDecodeError:
        sys.exit(84)

    i = 0
    for fdata in file_data:
        file_data[i] = fdata.rstrip()
        i += 1
    return file_data


def convert_to_baser64(hexa):
    try:
        base64 = binascii.b2a_base64(binascii.unhexlify(hexa))
    except Exception:
        sys.exit(84)
    print(base64.decode('utf-8').rstrip())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(84)

    try:
        hex = read_file()
    except IOError:
        sys.exit(84)

    if  len(hex) == 0:
        sys.exit(84)

    for line_hexa in hex:
        convert_to_baser64(line_hexa)

    sys.exit(0)