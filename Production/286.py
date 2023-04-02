# A問題
N, P, Q, R, S = map(int, input().split())
A             = list(map(int, input().split()))

change     = A[P - 1:Q]
A[P - 1:Q] = A[R - 1:S]
A[R - 1:S] = change

print(*A)

# B問題
N = int(input())
S = input()

print(S.replace('na', 'nya'))

# C問題 時間切れ
N, A, B = map(int, input().split())
S       = input()

result = 0

while True:
  if str(S) == str(S)[::-1]:
    print(result)
    exit()

  if N % 2 == 0:
    N //= 2
    for n in range(N):
      if 
  else:
    N //= 2
    for n in range(N):
      #

# D問題 不正解
N, X = map(int, input().split())
A = []
result = 0

for n in range(N):
  A.append(list(map(int, input().split())))

A.reverse()

for n in range(N):
  for a in range(A[n][1]):
    if result + A[n][0] <= X:
      result += A[n][0]

if result == X:
  print('Yes')
else:
  print('No')