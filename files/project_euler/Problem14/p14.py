def find_collatz_sequence_len(start):
    sequence = [start]
    while(sequence[-1] != 1):
        if(sequence[-1] % 2 == 0):
            sequence.append(sequence[-1]/2)
        else:
            sequence.append(sequence[-1]*3 + 1)
    return len(sequence)


def find_biggest_collatz_sequence(limit):
    highest_sequence_len = 0
    starting_number = 0
    for i in range(1, limit+1):
        len = find_collatz_sequence_len(i)
        if(len > highest_sequence_len):
            highest_sequence_len = len
            starting_number = i
            print(f"Number for try: {i}")
            print(f"New highest sequence: {highest_sequence_len}")
    return starting_number


if __name__ == "__main__":
    print(find_biggest_collatz_sequence(1000000))
