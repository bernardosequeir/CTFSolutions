import base64
from Crypto.Cipher import AES 

key =base64.b64decode("r7y1dhmTvjQrcra7A1UQFw==")
ciphertext= base64.b64decode("V3Vqirostg6qW26sle5mnyrwEYSrteN6oHkilO50e9dFkN+0JhC3yu0LcQNw/hXU")
crypter = AES.new(key, AES.MODE_ECB)
plaintext = crypter.decrypt(ciphertext).decode("utf-8")

print(plaintext)