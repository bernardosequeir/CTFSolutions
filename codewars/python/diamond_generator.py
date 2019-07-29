def diamond(n):
  if (n <= 0) or (n % 2 == 0 ):
    return None
  i = 1 
  diamond_str = ''
  while i <= n:
    space_num = int((n - i) / 2)
    diamond_str+= ' '*space_num +  i * '*' +  '\n'
    i+=2
  i-=4  
  while i >=1:
    space_num = int((n - i) / 2)
    diamond_str+= ' '*space_num +  i * '*' +  '\n'
    i-=2
  return diamond_str
     

print (diamond(0))
print (diamond(5))
print (diamond(2))