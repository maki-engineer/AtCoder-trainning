import math

P = int(input())

count  = 0
result = 0

for i in range(10, 0, -1):
  if P >= math.factorial(i):
    count   = P // math.factorial(i)
    result += P // math.factorial(i)
    P      -= math.factorial(i) * count

print(result)