print("Set 1 Challenge 2 - Fixed XOR\n")


def bitwise_xor(s1, s2):
    return bytes(a ^ b for (a, b) in zip(s1, s2))


from binascii import unhexlify

S1 = unhexlify('1c0111001f010100061a024b53535009181c')
S2 = unhexlify('686974207468652062756c6c277320657965')

expected = unhexlify('746865206b696420646f6e277420706c6179')

print(expected)
assert(bitwise_xor(S1, S2) == expected)
