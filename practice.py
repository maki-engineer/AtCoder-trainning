s = input()

check = False

if s[0] != 'A': check = True

if 'C' not in s[2:-2]:
  check = True
else:
  ci    = s[2:-2].find('C')
  s     = s[1:ci + 2] + s[ci + 3:]

if not s.islower(): check = True

if check:
  print('WA')
else:
  print('AC')
