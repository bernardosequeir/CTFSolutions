arr = [186,249,356,395,303,337,190,393,146,174,446,127,385,400,420,226,76,294,144,90,291,445,137]
converted_arr = list(map(lambda x: pow(x , -1, 41), arr))

def convert_char(char_code):
    if(char_code == 37): return '_'
    if(char_code >= 27): return chr(48 - 27 + char_code)
    return chr(64 + char_code)

def convert_arr(arr): 
    return "".join(list(map(convert_char, arr)))


print(convert_arr(converted_arr))