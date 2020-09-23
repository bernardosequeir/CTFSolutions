import math
def round_to_next5(n):
  return int(math.ceil(n/5) + 1) * 5


print(round_to_next5(4))
print(round_to_next5(5))
print(round_to_next5(-5))
