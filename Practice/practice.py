N = int(input())

result = 0

for n in range(1, N + 1):
  if (n % 3 != 0) and (n % 5 != 0):
    result += n

print(result)