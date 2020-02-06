def solution(string, ending):
  return string[-len(ending):] == ending
solution('abcde', 'cde')
solution('abcde', 'abc')