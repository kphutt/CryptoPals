print("Set 1 Challenge 2 - Fixed XOR\n")


def xor_strings(s1, s2):
    bytes1 = bytes.fromhex(s1)
    bytes2 = bytes.fromhex(s2)

    result = bytes.hex(bytes(a ^ b for (a, b) in zip(bytes1, bytes2)))

    print("S1 XOR S2 = " + result)
    return result


xor_strings("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
