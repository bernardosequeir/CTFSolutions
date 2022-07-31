key = 'CYLABCYLABCYLABCYLABCYLABCYLABCYLABCYLABCY'

def decrypt(cypher):
    plain = ''
    key_location = 0
    for i in range(len(cypher)):
        if not cypher[i].isalpha():
            plain += cypher[i]
        else: 
            if cypher[i].islower(): 
                plain += chr((ord(cypher[i]) - ord(key[key_location].lower())) % 26 + 97)
            else: 
                plain += chr((ord(cypher[i]) - ord(key[key_location])) % 26 + 65)
            key_location += 1
    return plain

if __name__ == '__main__':
    print(len('rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}'))
    print(decrypt('rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}'))    