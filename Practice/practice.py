N = int(input())

S      = []

for n in range(N):
  count  = 0
  i, num = n, n + 1

  while True:
    if num % 2 == 0:
      num   /= 2
      count += 1
    else:
      break

  S.append(count)

print(S.index(max(S)) + 1)