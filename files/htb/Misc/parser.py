with open('machine_list.txt') as retired_machines, open('machines.md', 'w') as md:
  base_href = 'https://www.hackthebox.eu'
  easy_machines = ''
  medium_machines = ''
  hard_machines = ''
  insane_machines = ''
  for line in retired_machines:
    if 'difficulty d' in line:
      l = retired_machines.readline()
      box_name = l.split(
          'data-original-title=')[2].split('>')[1].split('<')[0]
      path = l.split('href="')[1].split('"')[0]
      if ' fa-chevron-circle-up text-info' in l:
        ip_addr = l.split('class="ip">')[1].split('<')[0]
      else:
        ip_addr = retired_machines.readline().split('>')[1].split('<')[0]
      box_info = '* [' + box_name + ' - ' + \
          ip_addr + '](' + base_href + path + ')\n'
      print('* [' + box_name + ' - ' + ip_addr + '](' + base_href + path + ')')
      if 'easy' in line:
        easy_machines += box_info
      elif 'medium' in line:
        medium_machines += box_info
      elif 'hard' in line:
        hard_machines += box_info
      elif 'insane' in line:
        insane_machines += box_info
  md.write("### Easy Machines\n")
  md.write(easy_machines)
  md.write("### Medium Machines\n")
  md.write(medium_machines)
  md.write("### Hard Machines\n")
  md.write(hard_machines)
  md.write("### Impossible Machines\n")
  md.write(insane_machines)
