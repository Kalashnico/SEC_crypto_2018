#!/usr/bin/env python3.6

import sys


def read_file():
    file = open(sys.argv[1], "r")
    file_data = file.readlines()

    hex_key = file_data[0].rstrip()
    hex_string = file_data[1].rstrip()

    hex_key_to_list = []

    n = 0
    while True:
        for i in range(0, len(hex_key)):
            if len(hex_key_to_list) == len(hex_string):
                break
            hex_key_to_list.append(hex_key[i])
            n += 1

        if len(hex_key_to_list) < len(hex_string):
            continue
        else:
            break

    hex_key_list_to_string = ''.join(hex_key_to_list)
    key_list_to_string = ''.join(hex_string)

    xored = hex(int(hex_key_list_to_string.strip(), 16) ^ int(key_list_to_string.strip(), 16)).lstrip('0x')
    print(xored.upper())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(84)

    try:
        read_file()
    except IOError:
        sys.exit(84)

    sys.exit(0)