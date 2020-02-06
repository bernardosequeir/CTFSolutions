# script to find if some of the files in /balance-transfer was smaller than the others
with open('./index.html') as files:
  file_sizes = []
  for f in files:
    file_sizes.append(f.split('<td align="right">')[2].split(' </td>')[0])
  print(sorted(file_sizes))
