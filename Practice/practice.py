import math

A, B = map(int, input().split())

for n in range(1, 10001):
  a, b = math.floor(n * 0.08), math.floor(n * 0.1)

  if a == A and b == B:
    print(n)
    exit()

print(-1)