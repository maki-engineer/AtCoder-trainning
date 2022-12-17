N, A, B = map(int, input().split())

result = 0

def digitSum(n):
  s = str(n)

  array = list(map(int, s))

  return sum(array)

for n in range(1, N + 1):
  num = digitSum(n)

  if A <= num <= B: result += n

print(result)