S, str_len, check = input(), 5, False

while S:
  check_str = S[:str_len]

  if str_len == 5:
    if (check_str == 'dream') or (check_str == 'erase'):
      check = True

    str_len += 1

  elif str_len == 6:
    if check_str == 'eraser':
      S       = S[str_len:]
      str_len = 5
    else:
      if check:
        str_len = 5
        S       = S[str_len:]
        check   = False
      else:
        str_len += 1

  else:
    if check_str != 'dreamer':
      if check:
        str_len = 5
        S       = S[str_len:]
        check   = False
      else:
        print('NO')
        exit()
    else:
      S       = S[str_len:]
      str_len = 5

print('YES')