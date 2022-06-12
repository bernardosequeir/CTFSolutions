encoded_flag = open('enc', 'r').read()

flag = ''

for i in range(len(encoded_flag)): 
    flag += chr((ord(encoded_flag[i]) >> 8))
    flag += chr((ord(encoded_flag[i]))-((ord(encoded_flag[i])>>8)<<8)) 

print(flag)