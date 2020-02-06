def dashatize(num):
  dash_str=''
  num_str = str(num)
  for x in range(len(num)):
    if x == len(num_str):
        


print(dashatize(274)) #2-7-4", "Should return 2-7-4")
print(dashatize(5311)) #"5-3-1-1", "Should return 5-3-1-1")
print(dashatize(86320)) #"86-3-20", "Should return 86-3-20")
print(dashatize(974302)) #"9-7-4-3-02", "Should return 9-7-4-3-02")
print(dashatize(None) )#"None", "Should return None");
print(dashatize(0)) #"0", "Should return 0");
print(dashatize(-1)) #"1", "Should return 1");
print(dashatize(-28369)) #"28-3-6-9", "Should return 28-3-6-9")