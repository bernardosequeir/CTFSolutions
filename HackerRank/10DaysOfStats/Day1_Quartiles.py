size = int("10")

number_list = sorted(list(map(int, "3 7 8 5 12 14 21 15 18 14".split())))
if(size % 2 != 0):
    first_half = number_list[:size//2]
    second_half = number_list[(size//2)+1:]
else:
    first_half = number_list[:size//2+1]
    second_half = number_list[(size//2):]
if(len(first_half) % 2 == 0):
    print(int((first_half[len(first_half)//2] +
               first_half[(len(first_half)//2)-1])/2))
else:
    print(first_half[len(first_half)//2])
if(len(number_list) % 2 == 0):
    print(int((number_list[len(number_list)//2] +
               number_list[(len(number_list)//2)-1])/2))
else:
    print(number_list[len(number_list)//2])
if(len(second_half) % 2 == 0):
    print(int(round((second_half[len(second_half)//2] +
                     second_half[(len(second_half)//2)-1])/2, 0)))
else:
    print(second_half[(len(second_half)//2)])
