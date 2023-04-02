# A問題
N = int(input())
S = input()

if N == 1:
  print('Yes')
  exit()

for n in range(1, N):
  if S[n] == S[n - 1]:
    print('No')
    break
else:
  print('Yes')

# B問題
num = 9

for _ in range(8):
  s    = list(input())
  num -= 1
  if '*' in s:
    num   = str(num)
    index = s.index('*')
    alpha = chr(ord("a") + index)
    print(alpha + num)
    exit()

# C問題 不正解
N, X = map(int, input().split())
A    = list(map(int, input().split()))

def check(ary):
  for a in A:
    check = X + a
    if check in A:
      return True

  return False

print('Yes' if check(A) else 'No')