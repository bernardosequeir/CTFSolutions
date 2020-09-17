size = int(input())
values_list = list(map(int, input().split()))
frequency_list = list(map(int, input().split()))
numbers = []

for i in range(size):
    numbers += [values_list[i]] * frequency_list[i]

numbers = sorted(numbers)
lower_quartile = 0
higher_quartile = 0

if(size % 2 != 0):
    first_half = numbers[:size//2]
    second_half = numbers[(size//2)+1:]
else:
    first_half = numbers[:size//2+1]
    second_half = numbers[(size//2):]
if(len(first_half) % 2 == 0):
    lower_quartile = (first_half[len(first_half)//2] +
                      first_half[(len(first_half)//2)-1])/2
else:
    lower_quartile = first_half[len(first_half)//2]
if(len(second_half) % 2 == 0):
    higher_quartile = round((second_half[len(second_half)//2] +
                             second_half[(len(second_half)//2)-1])/2, 0)
else:
    higher_quartile = second_half[(len(second_half)//2)]
print(higher_quartile)
print(first_half)
print(round(higher_quartile - lower_quartile, 1))
