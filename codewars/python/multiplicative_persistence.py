def persistence(n):
  i = 0
  while (len(str(n)) > 1):
    mul = 1
    for num in str(n):
      mul *= int(num)
      n = str(mul)
    i+=1
  return i

print(persistence(39))# 3
print(persistence(4))# 0
print(persistence(25))# 2
print(persistence(999))# 4
