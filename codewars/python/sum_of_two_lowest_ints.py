def sum_two_smallest_numbers(numbers):
  lowest_one = numbers[0]
  lowest_two = numbers[1]
  for i in numbers[2:]:
    if i < lowest_one:
      old_lowest = lowest_one
      lowest_one = i
      if old_lowest < lowest_two:
        lowest_two = old_lowest
    elif i < lowest_two:
      lowest_two = i
  return lowest_one + lowest_two


print("Basic tests")
print(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
