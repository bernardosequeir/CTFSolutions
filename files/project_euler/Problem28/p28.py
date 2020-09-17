def create_matrix(size):
    matrix = [[0 for x in range(size)] for y in range(size)]
    value = 1
    turn_size = 1
    w, h = int(size/2), int(size/2)
    while(value < size ** 2):
        if(turn_size == 1):
            print(str(w) + " " + str(h))
            matrix[w][h] = value
            w += 1
            value += 1
        for move in range(turn_size):
            print(str(w) + " " + str(h))
            matrix[w][h] = value
            value += 1
            h += 1
        for move in range(turn_size):
            print(str(w) + " " + str(h))
            matrix[w][h] = value
            value += 1
            w -= 1
        for move in range(turn_size):
            print(str(w) + " " + str(h))
            matrix[w][h] = value
            value += 1
            h -= 1
        for move in range(turn_size):
            print(str(w) + " " + str(h))
            matrix[w][h] = value
            value += 1
            w += 1
        h -= 1
        w += 1
    return matrix


def print_matrix(matrix):
    for row in matrix:
        values = ""
        for value in row:
            values += str(value) + " "
        print(values)


if __name__ == "__main__":
    matrix = create_matrix(5)
    print_matrix(matrix)
