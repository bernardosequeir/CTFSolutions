def count(array):
  count_dict = {}
  for string in array:
    if string not in count_dict:
      count_dict[string] = 1
    else:
      count_dict[string] += 1
  return count_dict


print(count(['a', 'a', 'b', 'b', 'b']))  # { 'a': 2, 'b': 3 }
