N = int(input())

while N >= 1000:
  N -= 1000

if N > 0: N = 1000 - N

print(N)