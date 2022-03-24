print("Set 1 Challenge 1 - Convert hex to base64\n")


def hex_to_base_64(value):
    import base64
    raw_bytes = bytes.fromhex(value)
    result = base64.b64encode(raw_bytes).decode()
    print("Hex to Base 64: " + result)
    return result


hex_to_base_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
