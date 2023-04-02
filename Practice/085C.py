N, Y = map(int, input().split())

a, b, c = -1, -1, -1

for i in range(N + 1):
  for j in range(N + 1):
    if (i) + (j) + (abs(N - i - j)) == N and (10000 * i) + (5000 * j) + (1000 * (N - i - j)) == Y:
      a, b, c = i, j, N - i - j

print(a, b, c)