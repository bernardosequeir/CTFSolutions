def alphabet_position(text):
    string = ""
    for char in text:
        if(ord(char) >= ord('A') and ord(char) < ord('a')):
            string += str(ord(char) - ord('A') + 1)
            string += " "
        elif ord(char) - ord('a') >= 0:
            string += str(ord(char) - ord('a') + 1)
            string += " "
    return string[:-1]
