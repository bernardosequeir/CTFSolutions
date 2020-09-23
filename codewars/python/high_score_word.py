def high(x):
    a_value = ord('a')
    word_arr = x.split(" ")
    high_word = ""
    high_score = 0
    
    for word in word_arr:
        word_score = 0
        for c in word: 
            word_score += ord(c) - a_value + 1
        if (word_score > high_score):
            high_score = word_score
            high_word = word
    
    return high_word

print(high('man i need a taxi up to ubud')) #taxi
print(high('what time are we climbing up the volcano')) #volcano
