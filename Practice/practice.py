N, X, T = map(int, input().split())

result = 0
count  = 0

while count < N:
  count  += X
  result += T

print(result)