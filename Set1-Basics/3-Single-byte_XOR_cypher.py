# https://cryptopals.com/sets/1/challenges/3
print('Set 1 Challenge 3 - Single byte XOR cypher')


# http://www.brianveitch.com/maze-runner/frequency-analysis/index.html

def bxor(s1, s2):
    # bitwise XOR
    return bytes(a ^ b for (a, b) in zip(s1, s2))


def freq_points(s):
    return s


def frequency_check(msg):
    from string import printable

    xor_most_frequent = ''
    for letter in printable:
        frequency = 0
        xor_result = ''
        for val in msg:
            xor_result += bitwise_xor(val, letter)

        print("[" + letter + "] " + xor_result)

    return s


from binascii import unhexlify

A = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

key = b'\x02'
keystream = key * len(A)
print(bxor(A, keystream))

# frequency_check(A)
