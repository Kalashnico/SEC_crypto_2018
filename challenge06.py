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
	return '{:x}'.format(best_score_key).upper()

def find_best_key(crypted_text, keys):
	results = []
	scores = []
	key_index = 0

	for key in keys:
		result = ''
		index = 0
		for char in crypted_text:
			result += ''.join(chr(char ^ ord(key[index])))
			if index + 1 == len(key):
				index = 0
			else:
				index +=1
		results.append(result)
		scores.append(get_english_score(results[key_index]))
		key_index += 1

	best_key = scores.index(max(scores))
	print(keys[best_key])


def break_repeating_xor(crypted_text):
	average_distances = []

	for keysize in range(5, 41):
		distances = []
		chunks = [crypted_text[i : i + keysize] for i in range(0, keysize * 2, keysize)]

		chunk1 = chunks[0]
		chunk2 = chunks[1]

		distances.append(calculate_hamming_distance(chunk1, chunk2) / keysize)

		result = {
			'key': keysize,
			'average_distance': sum(distances) / len(distances)
		}

		average_distances.append(result)

	key_lengths = sorted(average_distances, key=lambda x: x['average_distance'])[:5]
	keys = []

	for key_length in key_lengths:
		key = ''
		for i in range(key_length['key']):

			block = b''

			for j in range(i, len(crypted_text), key_length['key']):
				block += bytes([crypted_text[j]])

			key += decipher(block)

		keys.append(key)

	find_best_key(crypted_text, keys)

def calculate_hamming_distance(bytes1, bytes2):
	hamming_distance = 0
	for b1, b2 in zip(bytes1, bytes2):
		difference = b1 ^ b2
		hamming_distance += sum([1 for bit in bin(difference) if bit == '1'])

	return hamming_distance

if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.exit(84)

	try:
		files_contents = read_file()
	except IOError:
		sys.exit(84)

	if len(files_contents) == 0:
		sys.exit(84)

	hex_str = files_contents.strip('\n')
	break_repeating_xor(binascii.unhexlify(hex_str))

	sys.exit(0)