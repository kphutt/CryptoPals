# https://cryptopals.com/sets/1/challenges/3
print('Set 1 Challenge 3 - Single byte XOR cypher')

from binascii import unhexlify
from string import printable


def bxor(s1, s2):
    """Bitwise XOR of two byte strings."""
    return bytes(a ^ b for (a, b) in zip(s1, s2))


def score_plaintext(text):
    """Score text by English letter frequency. Higher = more likely English."""
    freq = {
        'e': 13, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7, 'n': 6.7, 's': 6.3,
        'h': 6.1, 'r': 6, ' ': 15
    }
    return sum(freq.get(chr(b).lower(), 0) for b in text)


ciphertext = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

best_score = 0
best_result = b''
best_key = 0

for key in range(256):
    keystream = bytes([key]) * len(ciphertext)
    plaintext = bxor(ciphertext, keystream)
    score = score_plaintext(plaintext)
    if score > best_score:
        best_score = score
        best_result = plaintext
        best_key = key

print(f"Key: {best_key} ('{chr(best_key)}')")
print(f"Plaintext: {best_result}")
