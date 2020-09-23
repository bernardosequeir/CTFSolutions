def tribonacci(signature, n):
  if (n == 0):
    return []
  elif (n -3 <= 0):
    return signature[:n] 
  sequence = signature
  i=0
  
  while i<(n-3): 
    a, b, c = sequence[-3:]
    sequence.append(a+b+c)
    i+=1
  return sequence

print(tribonacci([1, 1, 1], 10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10)) # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([0, 1, 1], 10)) # [0, 1, 1, 2, 4, 7, 13, 24, 44, 8 ]
print(tribonacci([8, 20, 10], 2)) # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]