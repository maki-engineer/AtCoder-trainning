N = int(input())

result = 0
money  = 0
num    = 1

while True:
  if money >= N: break

  money  += num
  num    += 1
  result += 1

print(result)