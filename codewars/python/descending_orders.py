def Descending_Order(num):
  return ''.join([int(i) for i in str(num)].sort())


print(Descending_Order(0), 0)
print(Descending_Order(15), 51)
print(Descending_Order(123456789), 987654321)
