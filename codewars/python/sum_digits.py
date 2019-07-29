def sumDigits(number):
  sum = 0
  for c in str(number):
    if c.isdigit():
      sum+=int(c)
  return sum

print(sumDigits(10)) #10
print(sumDigits(99)) #18
print(sumDigits(-32)) #18