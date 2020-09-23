def divisors(n):
  n_divisors = 1
  i=2
  while i <= n:
    if (n % i == 0):
      n_divisors+=1
    i+=1 
  return n_divisors