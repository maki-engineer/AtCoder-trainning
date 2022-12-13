s = input()

check = False

if s[0] != 'A': check = True

if s[2:-1].count('C') != 1:
  check = True
else:
  ci    = s[2:-1].find('C')
  s     = s[1:ci + 2] + s[ci + 3:]

if not s.islower(): check = True

if check:
  print('WA')
else:
  print('AC')
