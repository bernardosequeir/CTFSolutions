i = 1
j = 1
below_or_equal = 0
while (i <= 6):
    while (j <= 6):
        if(i + j <= 9):
            below_or_equal += 1
        j += 1
    i += 1

print(below_or_equal)
