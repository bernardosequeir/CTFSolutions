
packet_data = open(r"C:\Users\Bernardo\Desktop\AMCQT\ctf\PicoCTF\Level2\just_keyp_trying\plaintext.txt", 'r')
#we just want the leftover bytes so we need to parse the packet data

def get_bytes(p_data):
    l_data = []
    for line in p_data:
        if(line.startswith("Leftover")):
            l_data.append(line.split(" ")[3].split("\n")[0][4:6])
                
    return l_data
def key_codes():
    key_codes = {}
    i = 4
    letter = 'a'
    while (i < 30):
        key_codes[i] = letter
        i+=1
        letter = chr(ord(letter) + 1)
    letter = '1'    
    while(i < 39):
        key_codes[i] = letter
        letter = chr(ord(letter) + 1)
        i+=1
    key_codes[i] = '0'
    return key_codes

def decypher_text(key_codes, leftover_data):
    plaintext = ""
    for byte in leftover_data:
        if(byte != '00'):
            if(int(byte,16) in key_codes):
                plaintext+= key_codes[int(byte,16)]
    return plaintext            



k_codes = key_codes()
# print(k_codes)
leftover_data = get_bytes(packet_data)
print(leftover_data)        
plaintext = decypher_text(k_codes, leftover_data)
print (plaintext)