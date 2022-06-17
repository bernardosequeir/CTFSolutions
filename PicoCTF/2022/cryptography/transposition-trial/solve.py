def decrypt(cipher_text):
    aux = ''
    i = 2
    while(i < len(cipher_text)):
        aux += cipher_text[i]
        aux += cipher_text[i-2]
        aux += cipher_text[i-1]
        i+=3
    return aux



if __name__ == '__main__':
    print(decrypt('heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7%'))
