def encode(message, key):
  base_val = ord('a') - 1
  i = 0
  cyphertext = []
  for c in message:
    cyphertext.append(ord(c)-base_val+list(map(int, str(key)))[i % 4])
    i = i + 1


print(encode("scout", 1939), [20, 12, 18, 30, 21])
print(encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
