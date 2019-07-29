def double_char(s):
    new_str = ""
    for c in s:
        new_str += c*2
        if c == " ":
            new_str+= "  "
    return new_str

print (double_char("String")) #"SSttrriinngg"
print (double_char("Hello World")) #"HHeelllloo  WWoorrlldd"
print (double_char("1234!_ ")) #"11223344!!__  "