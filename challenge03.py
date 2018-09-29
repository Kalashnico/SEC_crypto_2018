#!/usr/bin/env python3.6

import sys
import binascii

def get_english_score(string):

	character_frequencies = {
		'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
		'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
		'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
		'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
		'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
		'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
		'y': .01974, 'z': .00074, ' ': .19182
	}

	score = 0
	lower_string = string.lower()
	for char in lower_string:
		if char in character_frequencies:
			score += character_frequencies[char]
	return score

def read_file():
	file_open = open(sys.argv[1], "r")

	try:
		file_data = file_open.readline()
	except UnicodeDecodeError:
		sys.exit(84)

	return file_data

def decipher(hex_string):
	strings = []
	scores = []
	for key in range(256):
		strings.append(''.join(chr(char ^ key) for char in bytearray(hex_string)))
		scores.append(get_english_score(strings[key]))

	best_score_key = scores.index(max(scores))
	if best_score_key == 0:
		print ("00")
	else:
		print ('{:x}'.format(best_score_key).upper())

if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.exit(84)

	try:
		files_contents = read_file()
	except IOError:
		sys.exit(84)

	if len(files_contents) == 0:
		sys.exit(84)

	hex_str = binascii.unhexlify(files_contents.strip('\n'))
	decipher(hex_str)

	sys.exit(0)