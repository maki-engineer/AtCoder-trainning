# A問題
h, w  = map(int, input().split())
count = 0

for i in range(h):
  maps = input()
  maps = list(maps)

  for i2 in range(w):
    if maps[i2] == '#': count += 1

print(count)

# B問題
n = int(input())
s = input().split(' ')

int_s  = [int(i) for i in s]
result = [int_s[0]]

for i in range(1, n):
  result.append(int_s[i] - sum(result))

result = [str(i) for i in result]
result = " ".join(result)
print(result)

# C問題
s = input()
t = input()

result = 0
length = len(t)

s = list(s)
t = list(t)

s.append(" ")

for i in range(length):
  if s[i] != t[i]:
    result = i + 1
    break

print(result)

# D問題
def factorial_cor(n):
  fact = 1
  for integer in range(1, n + 1):
    fact *= integer
  return fact

print(factorial_cor(11))
print(39916800 / 11)