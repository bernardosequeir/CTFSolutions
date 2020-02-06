def odd_or_even(arr):
  sum=0
  for num in arr:
    sum+=num
  if ( sum % 2 == 0):
   return 'even'
  else:
    return 'odd'