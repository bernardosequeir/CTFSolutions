def iq_test(numbers):
  numbers_array = [int(i) for i in numbers]
  is_even = 0
  for num in numbers_array:
    if (num % 2 == 0):
      is_even += 1
  if is_even > 1:
    for i in range(len(numbers)):
      if (numbers[i] % 2 == 1):
        return i + 1
  else:
    for i in range(len(numbers)):
      if (numbers[i] % 2 == 0):
        return i + 1


iq_test("2 4 7 8 10")  # 3
iq_test("1 2 2")  # 1
