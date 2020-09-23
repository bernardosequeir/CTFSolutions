KEY = b'ICE'


def repeating_key_xor(key, plaintext):
    ciphertext = b""
    i = 0
    for char in plaintext:
        ciphertext += bytes([char ^ key[i % len(KEY)]])
        i += 1
    return ciphertext


def main():
    plaintext1 = b"Burning 'em, if you ain't quick and nimble"
    ciphertext1 = repeating_key_xor(KEY, plaintext1)
    print(str(ciphertext1))
    print("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272")
    plaintext2 = b"I go crazy when I hear a cymbal"
    ciphertext2 = repeating_key_xor(KEY, plaintext2)
    print(str(ciphertext2))
    print("a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")


if __name__ == "__main__":
    main()
