H, W = map(int, input().split())
S    = []

for i in range(H):
  S.append(list(input()))

for h in range(H):
  for w in range(W):
    if h == 0:
      if w == 0:
        if S[h][w] != '#':
          string = S[h][w + 1] + S[h + 1][w] + S[h + 1][w + 1]

          S[h][w] = str(string.count('#'))
      elif w == W - 1:
        if S[h][w] != '#':
          string = S[h][w - 1] + S[h + 1][w - 1] + S[h + 1][w]

          S[h][w] = str(string.count('#'))
      else:
        if S[h][w] != '#':
          string = S[h][w - 1] + S[h][w + 1] + S[h + 1][w - 1] + S[h + 1][w] + S[h + 1][w + 1]

          S[h][w] = str(string.count('#'))
    elif h == H - 1:
      if w == 0:
        if S[h][w] != '#':
          string = S[h - 1][w] + S[h - 1][w + 1] + S[h][w + 1]

          S[h][w] = str(string.count('#'))
      elif w == W - 1:
        if S[h][w] != '#':
          string = S[h - 1][w - 1] + S[h - 1][w] + S[h][w - 1]

          S[h][w] = str(string.count('#'))
      else:
        if S[h][w] != '#':
          string = S[h - 1][w - 1] + S[h - 1][w] + S[h - 1][w + 1] + S[h][w - 1] + S[h][w + 1]

          S[h][w] = str(string.count('#'))
    else:
      if w == 0:
        if S[h][w] != '#':
          string = S[h - 1][w] + S[h - 1][w + 1] + S[h][w + 1] + S[h + 1][w] + S[h + 1][w + 1]

          S[h][w] = str(string.count('#'))
      elif w == W - 1:
        if S[h][w] != '#':
          string = S[h - 1][w - 1] + S[h - 1][w] + S[h][w - 1] + S[h + 1][w - 1] + S[h + 1][w]

          S[h][w] = str(string.count('#'))
      else:
        if S[h][w] != '#':
          string = S[h - 1][w - 1] + S[h - 1][w] + S[h - 1][w + 1] + S[h][w - 1] + S[h][w + 1] + S[h + 1][w - 1] + S[h + 1][w] + S[h + 1][w + 1]

          S[h][w] = str(string.count('#'))

for i in range(H):
  print("".join(S[i]))