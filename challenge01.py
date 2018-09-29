#!/usr/bin/env python3.6

import sys
import binascii


def read_file():
    file_open = open(sys.argv[1], "r")
    file_data = file_open.readlines()

    i = 0
    for fdata in file_data:
        file_data[i] = fdata.rstrip()
        i += 1
    return file_data


def convert_to_baser64(hexa):
    base64 = binascii.b2a_base64(binascii.unhexlify(hexa))
    print(base64.decode('utf-8').rstrip())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(84)

    try:
        hex = read_file()
    except IOError:
        sys.exit(84)


    for line_hexa in hex:
        convert_to_baser64(line_hexa)

    sys.exit(0)