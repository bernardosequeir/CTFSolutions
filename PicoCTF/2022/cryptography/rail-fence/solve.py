def decode(cipher, rails):
    cipher_len = len(cipher)
    rail = [['\n' for i in range(len(cipher)) ] for j in range(rails)]    
    is_going_down = False
    row, col = 0,0 

    for i in range(len(cipher)): 
        if row == 0: 
            is_going_down = True
        elif row == rails -1: 
            is_going_down = False
        
        rail[row][col] = '*'
        col += 1

        if is_going_down: 
            row += 1
        else: 
            row -= 1
