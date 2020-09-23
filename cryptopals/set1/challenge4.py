from challenge3 import singlechar_xor_brute_force, pretty_print_result


def detect_singlechar_xor(encrypted_strings):
    candidates = []
    for string in encrypted_strings:
        candidates.append(singlechar_xor_brute_force(string))

    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]


def main():
    ciphertexts = [bytes.fromhex(line.strip())
                   for line in open("challenge4_input.txt")]
    most_likely_plaintext = detect_singlechar_xor(ciphertexts)
    pretty_print_result(most_likely_plaintext)


if __name__ == "__main__":
    main()
