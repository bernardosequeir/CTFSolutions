def isValidWalk(walk):
    x_axis = 0
    y_axis = 0
    for c in walk:
      # Iterating over each direction in the array, and updating the variables to make a sort of grid
        if (c == 'n'):
            y_axis += 1
        elif (c == 's'):
            y_axis -= 1
        elif (c == 'e'):
            x_axis += 1
        elif (c == 'w'):
            x_axis -= 1
    # If the last position is the same as the first one it's a real walk, and due to the requirements of the kata, it must have 10 directions
    if (len(walk) == 10) and x_axis == 0 and y_axis == 0:
        return True
    else:
        return False
