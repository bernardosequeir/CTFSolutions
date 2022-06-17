

ciphertext_alphabet = 'VOUHMJLTESZCDKWIXNQYFAPGBR'
plaintext_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(cipher_text):
    plaintext = ''
    for i in range(len(cipher_text)):
        index = ciphertext_alphabet.find(cipher_text[i].upper())
        if(index != -1):
            plaintext += plaintext_alphabet[index] if cipher_text[i].isupper() else plaintext_alphabet[index].lower()
        else : 
            plaintext += cipher_text[i] 

    return plaintext



if __name__ == '__main__':
    print(decrypt('Ytm jcvl eq: ieuwUYJ{5FO5717F710K_3A0CF710K_357OJ9JJ}'))
