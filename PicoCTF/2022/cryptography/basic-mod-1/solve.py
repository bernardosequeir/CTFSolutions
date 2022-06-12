arr = [128,63,242,87,151,147,50,369,239,248,205,346,299,73,335,189,105,293,37,214,333,137]
converted_arr = list(map(lambda x: x % 37, arr))

def convert_char(char_code):
    if(char_code == 36): return '_'
    if(char_code >= 26): return chr(48 - 26 + char_code)
    return chr(65 + char_code)

def convert_arr(arr): 
    return "".join(list(map(convert_char, arr)))


print(convert_arr(converted_arr))