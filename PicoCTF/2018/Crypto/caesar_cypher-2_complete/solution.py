cyphertext ="4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"
# shift = -100
# while (shift < 150):
#     newString = ""
#     for char in cyphertext:
#         if( ord(char)+shift>=0 and ord(char)+shift <256):
#             newString += chr(ord(char)+shift)
#     print newString
#     shift+=1
# print "DONE!"    
#     plainText += chr((ord(char) + 60) % 125)
# print plainText 
plainText = ""
for char in cyphertext:
    if (ord(char)+60 > 128):
        plainText += chr((ord(char) + 60) % 128 +34)
    else :
        plainText += chr((ord(char) + 60))    
print plainText