N, S = int(input()), input()

result = 0

for n in range(N):
  if n == 0: continue

  l, r = S[:n], S[n:]

  count = 0

  for c in 'abcdefghijklmnopqrstuvwxyz':
    if (c in l) and (c in r):
      count += 1

  result = max(result, count)

print(result)
