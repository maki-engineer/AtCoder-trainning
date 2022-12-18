import math

X = int(input())

money  = 100
result = 0

while True:
  if money >= X: break

  money   = math.floor(money * 1.01)
  result += 1

print(result)