print("Set 1 Challenge 1 - Convert hex to base64\n")


def hex_to_base_64(value):
    from base64 import b64encode
    from binascii import unhexlify
    result = b64encode(unhexlify(value))

    return result


hex_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
print(hex_to_base_64(hex_input) == expected)
